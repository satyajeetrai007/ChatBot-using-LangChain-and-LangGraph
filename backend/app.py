from services.chat_service import send_message
from services.chat_service import send_message_stream
from services.thread_service import create_thread
from flask import Flask, request, jsonify
from graph.graph import graph
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import BaseMessage, HumanMessage
from services.chat_service import send_message
from dotenv import load_dotenv

load_dotenv()  
app = Flask(__name__)


@app.route("/chat", methods = ["POST"])
def chat():
    data = request.get_json()
    user_input = data["message"]
    thread_id = data["thread_id"]

    if not user_input:
        return jsonify({"error" : "Message is Required"}), 400
    
    return send_message_stream(thread_id=thread_id, user_message=user_input)

# create a random thread name 
@app.route("/chat/new", methods=["POST"])
def handle_create_thread():
    """Endpoint for the frontend to request a new server-generated thread ID."""
    thread_data = create_thread()
    return jsonify(thread_data), 200


if __name__ == "__main__":
    app.run(debug=True)
