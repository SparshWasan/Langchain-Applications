from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("./attention_is_all_you_need.pdf")
doc = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

all_splits = text_splitter.split_documents(doc)

print(all_splits)
print(len(all_splits))
print(all_splits[0].metadata)