## Bank Transfer Anomaly Detection

This project implements an anomaly detection system for bank transfers using machine learning. It detects fraudulent or anomalous transactions using an Isolation Forest algorithm. The system consists of a **FastAPI backend** that serves predictions and a **Streamlit frontend** for user interaction.

### Features
- **Isolation Forest Model**: Trained to detect anomalous transactions with anomaly scoring
- **FastAPI Backend**: RESTful API with health checks and real-time predictions
- **Streamlit Frontend**: Interactive web interface for transaction analysis
- **Docker Containerization**: Full Docker and Docker Compose support for easy deployment
- **Input Validation**: Pydantic schemas with comprehensive field validation
- **Model Versioning**: Version tracking for model and API responses

### Model Details
The model (`fraud_isolation_forest_pipeline.pkl`, v1.0.0) analyzes transactions across multiple dimensions:
- **Account & Customer**: Account balance, customer age, occupation
- **Transaction**: Amount, duration, type (Credit/Debit), channel (ATM/Branch/Online)
- **Behavioral**: Login attempts, time since last transaction, location
- **Output**: Classification (Normal/Anomalous) with anomaly score

### Project Structure
```
Bank-Transfer-Anomaly-Detection/
├── api/
│   ├── app.py                 # FastAPI application with endpoints
│   └── __init__.py
├── ui/
│   └── main.py                # Streamlit frontend
├── model/
│   ├── fraud_isolation_forest_pipeline.pkl
│   ├── predict.py             # Model prediction logic
│   └── Fraud-Detection.ipynb   # Model training notebook
├── schema/
│   ├── user_input.py          # Input validation schema
│   └── prediction_response.py  # Response schema
├── data/
│   └── bank-transactions.csv   # Sample transaction data
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── Readme.md
```

### Installation

#### Option 1: Local Setup
1. Clone the repository and navigate to the project directory
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/Scripts/activate  # Windows
   # or
   source env/bin/activate      # macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Option 2: Docker
Build and run using Docker Compose:
```bash
docker-compose up --build
```

### Usage

#### Local Execution
1. Start the FastAPI backend:
   ```bash
   uvicorn api.app:app --reload --port 8000
   ```
2. In another terminal, start the Streamlit frontend:
   ```bash
   streamlit run ui/main.py
   ```
3. Access the application:
   - **API**: http://localhost:8000 (Swagger docs at `/docs`)
   - **Frontend**: http://localhost:8501

#### Docker Execution
Run with Docker Compose (automatically handles both services):
```bash
docker-compose up
```
- **API**: http://localhost:8000
- **Frontend**: http://localhost:8501

### API Endpoints

- **GET `/`** - Welcome message
- **GET `/health`** - Health check with model status and version
- **POST `/predict`** - Predict anomaly for transaction
  - Input: JSON with transaction details (see `schema/user_input.py`)
  - Output: Prediction ("Normal"/"Anomalous") and anomaly score

### Input Parameters
Transaction details required for prediction:
- Account Balance (float)
- Customer Age (int, ≥ 0)
- Login Attempts (int, ≥ 0)
- Transaction Amount (int, > 0)
- Transaction Duration (int, ≥ 0 seconds)
- Transaction Date (ISO 8601 format)
- Recent Transaction Date (ISO 8601 format)
- Channel (ATM / Branch / Online)
- Customer Occupation (Doctor / Engineer / Retired / Student)
- Location (string)
- Transaction Type (Credit / Debit)