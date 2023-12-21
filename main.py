import pypdf as pdf

reader = pdf.PdfReader('testdir/TEST.pdf')
number_of_pages = len(reader.pages)

print(number_of_pages)




for page in reader.pages:
    if "/Annots" in page:
        for annot in page["/Annots"]:
            subtype = annot.get_object()["/Subtype"]
            #print(subtype)
            if subtype == "/Highlight":
                coords = annot.get_object()["/QuadPoints"]
                print(coords)
                print(annot.get_object())
                print(len(coords))
                #print(coords)
                