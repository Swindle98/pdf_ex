import fitz
import yaml

def load_settings():
    '''
    Loads the settings from the settings.yaml file.
    '''
    with open("settings.yaml", "r") as yamlfile:
        settings = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Read successful")
        global pdf_dir
        pdf_dir = settings["pdf_dir"]
        global citation_notes_dir
        citation_notes_dir = settings["citation_notes_dir"]


def colour_name(colour):
    '''
    Converts a colour from RGB to a name. Based on the default colours in the Highlighs application, 
    other applications will just return colour values.
    '''
    if colour == (1.0, 0.75, 0.5):
        return "orange"
    if colour == (1.0, 0.5, 0.5):
        return "red"
    if colour == (1.0, 1.0, 0.5):
        return "yellow"
    if colour == (1.0,0.5,1.0):
        return "pink"
    if colour == (0.75, 0.5, 0.75):
        return "purple"
    if colour == (0.5, 1.0, 0.5):
        return "green"
    if colour == (0.5, 1.0, 1.0):
        return "blue"   
    else:
        return colour 

def highlight_info(annot, debug=False):
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

if __name__ == "__main__":

    doc = fitz.open(pdf_dir)

    annotations = []
    for page in doc:
        for annot in page.annots():
            annotation =  highlight_info(annot)
            if annotation:
                annotation.append(page.number)
                annotations.append(annotation)

    print(create_md_text(annotations))

