# Bank Branch API

This project implements an API server for querying bank branches and their details using FastAPI. It solves the assignment by creating REST API endpoints to read and serve bank data from a CSV file.

---

## 🚀 Solution Approach

✅ **Technology Used:**  
- Python
- FastAPI
- Uvicorn
- Pandas

✅ **Approach:**

- Loaded the provided bank data CSV file using **Pandas**.
- Created FastAPI routes:
  - `/banks` → Fetches the list of all unique banks.
  - `/banks/{bank_name}/branches` → Fetches all branches of a specified bank.
  - `/branches/{ifsc}` → Fetches branch details by IFSC code.
- Built a dictionary lookup for fast retrieval of branch details.
- Wrote test cases using **pytest** and FastAPI’s TestClient.
- Prepared the app for deployment on Heroku using a Procfile.

---

## ⏱ Time Taken

- Total time spent: **3 hours**

---

## 🗂 Project Structure

├── banks.csv
├── main.py
├── requirements.txt
├── test_main.py


---

## 🔧 How to Run Locally

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the API:
    ```bash
    uvicorn main:app --reload
    ```

3. Visit:
    - http://127.0.0.1:8000/banks
    - http://127.0.0.1:8000/banks/{bank_name}/branches
    - http://127.0.0.1:8000/branches/{ifsc}

---

## ✅ Running Tests

Run all tests:

```bash
pytest
