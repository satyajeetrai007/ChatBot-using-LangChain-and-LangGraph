from .nodes.chat_node import chat_node  # import chat_node from graph/nodes/chat_node.py
from langgraph.graph import StateGraph, START, END
from graph.state import StateDict
from llm import build_chat_model
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver


Chat_llm = build_chat_model(model_name="llama-3.1-8b-instant")
CheckPointer = InMemorySaver() # Short-Term Memory
workflow = StateGraph(StateDict)
    
# add Node 
workflow.add_node("Chat", chat_node)

# add edges
workflow.add_edge(START, "Chat")
workflow.add_edge("Chat", END)

# compile graph
graph = workflow.compile(checkpointer=CheckPointer) 



