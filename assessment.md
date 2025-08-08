# 🖊️ Mini E-Signature Flow – Technical Assessment

Welcome! This short assessment is designed to evaluate your ability to work across a modern full-stack web application. You'll be creating a simple document upload and signing workflow using Angular and Python.

---

## 🎯 Objective

This assessment should take you about 2 hours.

Build a minimal e-signature flow that allows a user to:

1. Upload a PDF file via a web interface.
2. Send the file to a Python backend.
3. "Sign" the document (simulate this with metadata).
4. Save the signed file locally on the backend (no cloud storage needed).
5. Display a success message and signing metadata in the frontend.



---

## 📂 Project Structure
e-signature-assessment/
│
├── backend/ # Python Flask backend
│ ├── app.py
│ └── requirements.txt
│
├── frontend/ # Angular frontend
│ └── [Angular app]
│
└── README.md

## 🚀 Setup Instructions

### 🔧 Backend

Run the backend Flask server:

cd backend
pip install -r requirements.txt
python app.py

## 🧩 Frontend
In another terminal, start the Angular app:
cd frontend
ng serve


## 🛠️ What You Need to Implement
Frontend (Angular)
Add an HTML form with:

A file input for selecting a PDF

A button to upload the file to the backend

Send the selected file using a POST request to /upload

Display a response with:

Filename

Timestamp (when it was "signed")

Add comments to your code where applicable

## 💡 You'll find the Angular app already scaffolded in frontend/src/app.

Backend (Python + Flask)
The backend has a /upload endpoint ready to receive files. You should:

Accept the uploaded file

Simulate a "sign" by:

Appending signing metadata (e.g., timestamp)

Saving the file locally in a signed_docs/ directory

Return a JSON response with the filename and timestamp

## 📝 You do not need to implement real cryptographic signing. Just simulate it in a simple way.

## 🧪 Example Flow
User selects contract.pdf

User clicks "Sign & Upload"

Frontend sends the file to /upload

Backend saves a file like signed_docs/contract-signed.pdf

Response is shown in the UI:

json
Copy
Edit
{
  "message": "File signed",
  "metadata": {
    "filename": "contract.pdf",
    "signed_at": "2025-06-24T12:03:00Z"
  }
}

## ✅ Notes
CORS is already enabled in the backend to allow communication from Angular.

The focus is on code clarity, communication between frontend and backend, and good structure — not pixel-perfect design or auth.