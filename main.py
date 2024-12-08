import pdfplumber

PATH = "data\LLMCloudHunter_print.pdf"


with pdfplumber.open(PATH) as pdf:
    page = pdf.pages[0]
    print("page:\n",page)
    text = page.extract_text()
    print()
    if text:
        print("text:\n",text)
    else:
        print("text:\n",None)