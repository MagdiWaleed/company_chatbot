from llama_index.core import (StorageContext,VectorStoreIndex,SimpleDirectoryReader)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from dotenv import load_dotenv
print(load_dotenv())

def generate_tools():

    embedd_model = GeminiEmbedding(
        model = 'models/embeddings-001'
    )
    llm = Gemini(model="models/gemini-2.5-flash")
    
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection("collection")
    vectorStorage = ChromaVectorStore(chroma_collection=collection)
    index = VectorStoreIndex.from_vector_store(vectorStorage, embed_model=embedd_model)
    query_engine = index.as_query_engine(llm=llm)

    def retriver(query:str)->str:
        """This tool helps the agent retrieve information from the documents.
        Args:
            - query: The question to ask for the query engine.
        Returns:
            - The answer to the question.
        Example:
            - query_engine("What is the capital of France?")
        Note: This tool is used by the agent to retrieve information from the documents.
        """
        return query_engine.query(query).response

    return retriver

