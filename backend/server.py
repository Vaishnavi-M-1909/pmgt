from flask import Flask, request, jsonify
from graph import pmgt_graph

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")

    response = pmgt_graph(message)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(port=8000)
