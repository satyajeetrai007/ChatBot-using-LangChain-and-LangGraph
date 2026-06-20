from llm import build_chat_model
from graph.state import StateDict
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv
load_dotenv()

chat_model = build_chat_model()
def chat_node(state:StateDict):
    message = [SystemMessage(content = "You are a helpful AI Assistant")] + state["messages"]
    response = chat_model.invoke(message)
    return {
        "messages":[response]
        }