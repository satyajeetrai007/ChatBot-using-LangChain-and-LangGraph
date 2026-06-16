from langchain_groq import ChatGroq


def build_chat_model(model_name):
    
    return ChatGroq(model= model_name)