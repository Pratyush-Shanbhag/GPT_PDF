import pdfplumber

with pdfplumber.open("ocr_output.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text().encode('utf-8')#.replace(b'\\n', b'\n')
    #print(text)
    #print('\n\n\n\n\n')
    #print(b''.join(text.splitlines()))

    f = open('ocr_to_text.txt', 'wb')
    f.write(text)
    f.close()

    print("ran")

'''from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader('output.pdf')
# Split pages from pdf 
pages = loader.load_and_split()

print(pages[0].page_content.encode('utf-8'))'''