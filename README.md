# Langchain Reproductive Health Bot

## 🎯 Motivations and Goals
### Motivations
- In the U.S., fewer than 50% of adolescents reported receiving education about accessing birth control or using condoms before their first sexual experience​
- Address gaps in reproductive health education
- Target audience: teenagers and YA
### Goals
- Create an LLM chatbot offering tailored, reliable advice on topics like birth control, STIs, abortion, and consent
- Chatbot compliments traditional education systems and supports informed decision-making 

## 🏆 Accomplishments

- **Second Place** @ [Data Science Varisty 2024](https://womeninbigdata-llm.hackerearth.com/)
- **Access our Submission**: [HackerEarth](https://womeninbigdata-llm.hackerearth.com/challenges/hackathon/llm-hackathon-2/dashboard/de1abe9/submission/)

## 🚀 Steps to Run the Project

- Make sure you have Node.js v18x and npm installed, then clone the repo & install dependencies
  
   ```bash
   git clone git@github.com:jsakeag/langchain-healthbot-new.git
   cd langchain-healthbot-new
   npm install

- Create a .env file and setup OpenAI API Key 

   ```bash
   REACT_APP_OPEN_AI_API_KEY=your_openai_api_key

- Start the Backend and Frontend Servers**:
   
   ```bash
   cd backend
   python3 app.py
   ```

   ```bash
   cd frontend
   npm start
   ```

## 💡 Q/A with our Neo4j Knowledge Graph

- Make sure `chatbot_response` import is `chatbot_KG.py` in the `app.py` file if you want to access our knowledge graph.
- Here is a code snippet showing how we initialized our knowledge graph and vector store:

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

- Make sure you allow your IP to access the endpoint so that you don't experience CORS errors

## 🛠️ Accessing Our Resources

### Neo4j Knowledge Graph
Here is a visual [link](https://workspace-preview.neo4j.io/workspace/query?ntid=google-oauth2%7C114513607131593483170) to our neo4j knowledge graph:

https://workspace-preview.neo4j.io/workspace/query?ntid=google-oauth2%7C114513607131593483170

### Web Scraper
Here is a [link]([url](https://colab.research.google.com/drive/1ubkOjOHJJ5TnD5pk7p4rXUMvesZP2CBW) to the code we used to downlaod and scrape articles neo4j:
https://colab.research.google.com/drive/1ubkOjOHJJ5TnD5pk7p4rXUMvesZP2CBW
