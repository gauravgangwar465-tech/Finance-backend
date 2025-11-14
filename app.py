from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Finance Companion Backend Running"}

@app.route("/add-expense", methods=["POST"])
def add_expense():
    data = request.json
    return {"status": "success", "data": data}

if __name__ == "__main__":
    app.run()
