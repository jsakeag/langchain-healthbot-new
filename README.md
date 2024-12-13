# Langchain Reproductive Health Bot

## Setup and Run the Project

### Prerequisites

- Node.js v18x and npm (If not installed, download from [Node.js official website](https://nodejs.org/))

### Steps

1. **Clone the Repository**:
   
   ```bash
   git clone git@github.com:jsakeag/langchain-healthbot-new.git
   cd langchain-healthbot-new

3. **Install Dependencies**:
   
   ```bash
   npm install
   ```

   If needed:
   ```bash
   pip install -r /path/to/requirements.txt

5. **Set Up OpenAI API Key**:

- Obtain your OpenAI API key.
- Create a .env file in the root directory and add your OpenAI key.

   ```bash
   REACT_APP_OPEN_AI_API_KEY=your_openai_api_key

6. **Start the Backend and Frontend Servers**:
   
   ```bash
   cd backend
   python3 app.py
   ```

   ```bash
   cd frontend
   npm start
   ```

## Options

1. **Q/A with our online KG**: The default way option uses a neo4j knowledge graph we created ourselves.
Notice that the `chatbot_response` import is from `chatbot_KG.py` in the `app.py` file.
Here is a code snippet from our chatbot_KG.py file:

```python
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
```

2. **ChatGPT Clone**: The other way to run this project is the ChatGPT default 4o mini model.
  This can be selected by setting the `chatbot_response` import to `chatbot.py` in the `app.py` file.
  Here is a code snippet from our chatbot.py file:

   ```python
   # Initialize OpenAI Chat model
   llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.7,
    max_tokens=500,
    api_key=openai_api_key  # Explicitly pass the API key here
   )
   # Initialize memory for conversation
   memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

   # Create embedding model
   embeddings = OpenAIEmbeddings(api_key=openai_api_key)  # Also pass the API key here

   # Initialize Chroma DB (vector database)
   vector_db = Chroma(embedding_function=embeddings, collection_name="my_collection",persist_directory="./my_chroma_db")
   ```

- If you are experiencing CORS errors Make sure you allow your IP to access the endpoint (look at your AWS lambda scripts)
