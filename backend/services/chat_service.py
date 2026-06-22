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
from flask import Response


def send_message(thread_id:str, user_message:str):

    config: RunnableConfig = {"configurable":{"thread_id": thread_id}, "metadata":{ "thread_id":thread_id}}   
    message = HumanMessage(content = user_message)
    result = graph.invoke({"messages":[(message)]}, config =config)
    return result


def send_message_stream(thread_id: str, user_message: str) -> Response:
    """
    Handles LangGraph streaming logic and returns a fully-formed 
    Flask Response object ready for the frontend.
    """
    config = {"configurable": {"thread_id": thread_id}}
    input_data = {"messages": [HumanMessage(content=user_message)]}
    
    def generate():
        for chunk, metadata in graph.stream(input_data, config=config, stream_mode="messages"):
            if chunk.content and metadata.get("langgraph_node") == "Chat":
                yield f"data: {chunk.content}\n\n"

    # Wrap the generator inside the helper function
    return Response(generate(), mimetype="text/event-stream")