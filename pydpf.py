import PyPDF2

PATH = "data\LLMCloudHunter.pdf"

with open(PATH, 'rb') as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = len(read_pdf.pages)
    # print(f"{read_pdf.pages=} {number_of_pages=}")

    try:
        pypdf_test = ""
        for page_number in range(number_of_pages): 
            page = read_pdf.pages[page_number]
            page_content = page.extract_text()
            sanitised_page_content = page_content.encode('ascii', 'replace').decode('ascii')
            pypdf_test += sanitised_page_content

        print(pypdf_test)

    except UnicodeEncodeError as e:
        print(f"Unicode error: {e}")