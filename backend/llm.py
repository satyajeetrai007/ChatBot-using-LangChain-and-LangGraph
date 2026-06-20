from langchain_groq import ChatGroq


def build_chat_model(model_name="llama-3.1-8b-instant"):
    
    return ChatGroq(model= model_name)