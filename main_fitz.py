import fitz
import re

doc = fitz.open("testdir/TEST.pdf")

def colour_name(colour):
    """
    Converts a colour from RGB to a name. Based on the default colours in the Highlighs application, 
    other applications will just return colour values.
    """
    if colour == (1.0458279848098755, 0.7369465231895447, 0.45456090569496155):
        return "orange"
    else:
        return colour

def highlight_info(annot, debug=False):
        """
        Returns the highlighted text, colour, comment and author of a highlight annotation.
        """
        if annot.type[0] != 8:
            """
            If the annotation is not a highlight, return None.
            """
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

        return [highlighted_text, colour, comment, author]



for page in doc:
    for annot in page.annots():
        annotation =  highlight_info(annot)
        if annotation:
            text = page.get_textbox(annotation[0])
        

