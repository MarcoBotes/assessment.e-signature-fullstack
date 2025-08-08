from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # allow Angular on localhost to talk to backend

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
   
    # Simulate "signing" by adding metadata (just returning it here)

    metadata = {
        "this is a test?": "yes"
    }
    
    # Save the file locally 
    
    return jsonify({"message": "File signed", "metadata": metadata}), 200

if __name__ == "__main__":
    app.run(debug=True)