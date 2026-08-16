from langchain_community.document_loaders import PyPDFLoader

file_path = "./PDF Content Previewer/attention_is_all_you_need.pdf"

loader = PyPDFLoader(file_path)
doc = loader.load()

print(doc[0].metadata)
print(doc[0].page_content)