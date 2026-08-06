import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .BaseController import BaseController
from src.models.enum.ExtensionEnum import ExtensionEnum

class ProcessController(BaseController):
    def __init__(self,project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_path = self.get_project_path(project_id=project_id)

    # 1- return the extension of the file    
    def get_file_extension(self, file_name: str) -> str:
        return os.path.splitext(file_name)[-1].lower()

    # 2- Know the loader based on the extension of the file and return it
    def get_file_loader(self, file_name: str):
        extension = self.get_file_extension(file_name)

        if extension == ExtensionEnum.TXT.value:
            return TextLoader(os.path.join(self.project_path, file_name),encoding='utf-8')

        if extension == ExtensionEnum.PDF.value:
            return PyPDFLoader(os.path.join(self.project_path, file_name))

        return None

    # 3- Load the file and return the content of the file as a list of documents
    def get_file_content(self, file_name: str):
        loader = self.get_file_loader(file_name)
        if loader is None:
            raise ValueError(f"Unsupported file extension for file: {file_name}")

        return loader.load() # this return a list of documents, each document is a dictionary with the keys: 'page_content' and 'metadata'

    # 4- Split the content in chunks with meaningful overlap and return the list of chunks
    # We prefare to use the RecursiveCharacterTextSplitter because it is more efficient and it can split the text in a more meaningful way
   

    def split_content_into_chunks(self, content: list, chunk_size: int = 1000,length_function=len):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,  
            chunk_overlap=200,
            length_function=length_function  # Function to measure the length of each chunk
        )
        # split every document and make two lists : content and metadata
        file_content = [doc.page_content for doc in content]
        file_metadata = [doc.metadata for doc in content]

        # Now we use text_splitter to make chunks  
        chunks = text_splitter.create_documents(file_content, metadatas=file_metadata) # make to each chunk linked to all metadata

        return chunks
    

