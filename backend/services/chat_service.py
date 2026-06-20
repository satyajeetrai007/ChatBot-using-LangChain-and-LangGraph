""" 

Responsibility:
    Build graph input
    Build config
    Invoke graph
    Return response

"""
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import HumanMessage
from graph.graph import graph

def send_message(thread_id:str, user_message:str):

    config: RunnableConfig = {"configurable":{"thread_id": thread_id}, "metadata":{ "thread_id":thread_id}}   
    message = HumanMessage(content = user_message)
    result = graph.invoke({"messages":[(message)]}, config =config)
    return result