from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

loader = TextLoader("./Python Code Splitter/tool_calling.py")
doc = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).from_language(language=Language.PYTHON)
all_splits = splitter.split_documents(doc)

print(len(all_splits))
print(all_splits[0].page_content)