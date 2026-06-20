from services.chat_service import send_message
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
    
    result = send_message(thread_id=thread_id, user_message=user_input)
   
    return jsonify(result["messages"][-1].content), 200


if __name__ == "__main__":
    app.run(debug=True)
