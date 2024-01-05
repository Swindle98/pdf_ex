import fitz
import yaml
import os
from scipy.spatial import KDTree


def load_settings():
    '''
    Loads the settings from the settings.yaml file as global variables.
    '''
    try:
        with open("settings.yaml", "r") as yamlfile:
            settings = yaml.load(yamlfile, Loader=yaml.FullLoader)
            print("Read successful", settings)
            print(settings['pdfs_dir'])

        global pdfs_dir
        pdfs_dir = settings['pdfs_dir']

        global citation_notes_dir
        citation_notes_dir = settings['citation_notes_dir']

        global tag
        tag = settings['tag']
    except:
        print("Error reading settings.yaml file")
        exit()
        
def colour_name(rgb_tuple):
    '''
    Converts an RGB tuple to a colour name.
    '''
    colour_db = {
        (1, 0.75, 0.5): "Orange",
        (1, 0.5, 0.5): "Red",
        (1, 1, 0.5): "Yellow",
        (1, 0.5, 1): "Pink",
        (0.75, 0.5, 0.75): "Purple",
        (0.5, 1, 0.5): "Green",
        (128, 1, 1): "Cyan",
        }
    
    
    names = []
    rgb_values = []    
    for rgb, color in colour_db.items():
        names.append(color)
        rgb_values.append(rgb)
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    print(names[index])
    return names[index]

"""def colour_name(colour):
    '''
    Converts a colour from RGB to a name. If the colour is not found, returns the RGB value.
    '''
    try:
        rgb_colour = (int(col * 256) for col in colour)
        print(colour)
        print(tuple(rgb_colour))
        colour_name = webcolors.IntegerRGB(rgb_colour)
        print(colour_name)
        #return colour_name
    except:
        print("Colour not found")
        return colour"""

def highlight_info(page, annot, debug=False):
        '''
        Returns the highlighted text, colour, comment and author of a highlight annotation.
        '''
        if annot.type[0] != 8:
            '''
            If the annotation is not a highlight, return None.
            '''
            
            return None
        
        a_type = annot.type[1]
        highlighted_text = page.get_textbox(annot.rect)
        colour = colour_name(annot.colors["stroke"])
        comment = annot.info["content"]
        author = annot.info["title"]

        if debug:
            print( f"""---------------------
debug for highlight_info(annot: {annot})
type: {a_type}
Author: {author}
colour: {colour}
comment: {comment}
highlighted_text: {highlighted_text}
---------------------
""")

        return [highlighted_text, a_type, colour, comment, author]


def create_md_text(annotations):
    '''
    Adds annotations to a pdf.
    '''
    full_md = "## PDF Annotations\n "
    for annot in annotations:
        if annot[1] == "Highlight":
            md_text = f"""### {annot[2]} highlight by {annot[4]} on page {annot[0][0]}:

>TEXT: 
> {annot[0]}

>COMMENT:
> {annot[3]}

"""
            full_md += md_text
    return full_md

def annotate_to_md(pdf):

    doc = fitz.open(pdf)
    annotations = []
    for page in doc:
        for annot in page.annots():
            annotation =  highlight_info(page, annot)
            if annotation:
                annotation.append(page.number)
                annotations.append(annotation)
    return create_md_text(annotations)

def md_search(citekey):
    '''
    Searches the citation_notes_dir for the citekey.md file and returns the path.
    '''
    for file in os.listdir(citation_notes_dir):
        if file == f"{citekey}.md":
            return os.path.join(citation_notes_dir, file)
    return None

def replace_string_in_file(file_path, old_string, new_string):
    '''
    Replaces a string in a file.
    '''
    # Open the file in read mode
    with open(file_path, 'r') as file:
        file_data = file.read()

    # Replace the target string
    file_data = file_data.replace(old_string, new_string)

    # Write the file out again
    with open(file_path, 'w') as file:
        file.write(file_data)

if __name__ == "__main__":
    load_settings()
    pdfs_dir_ls = os.listdir(pdfs_dir)
    print(pdfs_dir_ls)
    citekey_dict = {}
    for pdf in pdfs_dir_ls:
        if pdf[-4:] == ".pdf":
            
            citekey = pdf.split(" - ")[0]
            citekey_dict[citekey] = pdf

    print(citekey_dict)

    for key in citekey_dict:
        pdf = pdfs_dir + citekey_dict[key]
        notes = md_search(key)
        print(f"""
              PDF: {pdf}
              Notes: {notes}
              """)
        if notes:
            print(f"Found notes for {key}")
            md_text = annotate_to_md(pdf)
            replace_string_in_file(notes, tag, md_text)
        else:
            print(f"No notes found for {key}")

        
        
