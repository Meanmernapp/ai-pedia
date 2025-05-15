import os

import streamlit as st
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.readers.wikipedia import WikipediaReader
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage

load_dotenv()

INDEX_DIR = "wiki_rag"

PAGES = [
    "Artificial_intelligence",
    "Machine_Learning",
    "Neural_Network",
    "Reinforcement_Learning",
    "Supervised_learning",
    "Unsupervised_learning",
    "Natural_language_processing",
    # "Transformer",
    # "ML Model",
    # "ChatGPT",
    # "OpenAI",
    # "Computer vision",
    # "Generative adversarial network",
    # "Support vector machine",
    # "Decision tree learning",
    # "Gradient boosting",
    # "Bayesian network",
    # "K-nearest Neighbors algorithm",
    # "Feature Engineering",
    # "Deep Learning",
    # "Gen Ai",
    # "Ai AGents",
    # "Ai automation",
]


@st.cache_resource
def get_index():
    if os.path.isdir(INDEX_DIR):
        storage = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        return load_index_from_storage(storage)
    docs = WikipediaReader().load_data(pages=PAGES, auto_suggest=False)
    embedding_modal = OpenAIEmbedding(model="text-embedding-3-small")
    index = VectorStoreIndex.from_documents(docs, embed_model=embedding_modal)
    index.storage_context.persist(persist_dir=INDEX_DIR)
    return index


@st.cache_resource
def get_query_engine():
    index = get_index()
    llm = OpenAI(model="gpt-4o-mini", temperature=0)
    return index.as_query_engine(llm=llm, similarity_top_k=3)


def main():
    st.title("WikiPedia Rag System")
    # print("Hello from ragsystem!")
    quest = st.text_input("ASk  a question ?")
    if st.button("Search") and quest:
        with st.spinner("Thinking"):
            qa = get_query_engine()
            response = qa.query(quest)
        st.subheader("Answer")
        st.write(response.response)
        st.subheader("Retreived context")
        print(response.source_nodes)
        for src in response.source_nodes:
            st.markdown(src.node.text)


if __name__ == "__main__":
    main()
