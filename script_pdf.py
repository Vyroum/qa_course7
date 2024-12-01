from pypdf import  PdfReader



reader = PdfReader('tmp/Python-Testing-with-pytest.pdf')
print(reader.pages)
print(len(reader.pages))

print(reader.pages[1].extract_text())

assert "Simple" in reader.pages[1].extract_text()