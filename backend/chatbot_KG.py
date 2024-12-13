import os
from dotenv import load_dotenv
import openai
import neo4j
from langchain_neo4j import Neo4jGraph
from langchain_neo4j import Neo4jVector
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY");
endpoint = 'https://openai.com/v1/embeddings'
os.environ["OPENAI_API_KEY"] = openai.api_key

kg = Neo4jGraph(
    url="neo4j+s://4221dbdc.databases.neo4j.io",
    username = "neo4j",
    password="6wmPE5kyuqGAxoPBzZeB12Mb56gzaNpP9goIC-8qdAc",
    database = 'neo4j'
)

neo4j_vector_store = Neo4jVector.from_existing_graph(
    embedding=OpenAIEmbeddings(),
    url='neo4j+s://4221dbdc.databases.neo4j.io',
    username='neo4j',
    password='6wmPE5kyuqGAxoPBzZeB12Mb56gzaNpP9goIC-8qdAc',
    index_name='embeddings',
    node_label='Information',
    text_node_properties=['text'],
    embedding_node_property='embedding'
)

retriever = neo4j_vector_store.as_retriever()

chain = RetrievalQAWithSourcesChain.from_chain_type(
    ChatOpenAI(temperature=0),
    chain_type="stuff",
    retriever=retriever
)

def chatbot_response(question: str) -> str:
    """Pretty print the chain's response to a question"""
    response = chain({"question": question},
        return_only_outputs=True,)
    return response['answer']