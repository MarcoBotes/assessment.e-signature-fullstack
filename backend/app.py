import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime

from Utilities.config import Constants, Environment

app = Flask(__name__)
CORS(app)

# Create save directory if its not there
os.makedirs(Constants.directory, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        file = request.files.get("file")

        # Generic check for if its not a PDF
        if not file or not file.filename.endswith(".pdf"):
            return jsonify({"error": "Invalid file"}), 400

        # Clause I added to test the front-end
        if not Environment.is_production and 'fail_now_please' in file.filename:
            return jsonify({"error": "The API was designed to fail predictably when you upload a file with that name"}), 400

        # Transparently, haven't done a lot of PDF manipulation but a language model suggested this and gave me a working sample
        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        # Adding random metadata to the PDF
        metadata = {
            "/SignedBy": "Marco",
            "/SignedAt": str(datetime.now()),
            "/Purpose": "Test signing"
        }
        writer.add_metadata(metadata)

        # Save PDF
        output_path = os.path.join(Constants.directory, f"signed_{file.filename}")
        with open(output_path, "wb+") as f:
            writer.write(f)

        # Respond with the metadata and the filepath
        return jsonify({
            "message": "File signed",
            "metadata": metadata,
            "saved_to": output_path
        }), 200
    except Exception as ex:
        return jsonify({
            "error": str(ex)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)