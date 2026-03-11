## Bank Transfer Anomaly Detection

This project implements an anomaly detection system for bank transfers using a machine learning model. The system consists of a FastAPI backend that serves the model and a Streamlit frontend for user interaction. The model is trained to identify anomalous transactions based on various features of the transfer data.

### Features
- **FastAPI Backend**: Provides endpoints for health checks and predictions.
- **Streamlit Frontend**: Allows users to input transaction data and view predictions in a
    user-friendly interface.
- **Model Versioning**: The API includes version information in its responses for better tracking and maintenance.

### Model
The model is trained on a dataset of bank transfers and is designed to detect anomalies based on patterns in the data. It uses a combination of features such as transaction amount, time, and other relevant attributes to make predictions.

### Project Structure
```
Bank-Transfer-Anomaly-Detection/
├── api/
│   ├── app.py
│   ├── models.py
│   └── routes.py
├── ui/
│   └── main.py
├── models/
│   └── anomaly_detector.pkl
├── data/
│   ├── train.csv
│   └── test.csv
├── notebooks/
│   └── model_training.ipynb
├── requirements.txt
├── README.md
```

### Installation
1. Clone the repository:
   ```bash
   git clone
    ```
2. Navigate to the project directory:
    ```bash
    cd Bank-Transfer-Anomaly-Detection
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
### Usage
1. Start the FastAPI backend:
   ```bash
   uvicorn api.app:app --reload
   ```
2. In a separate terminal, start the Streamlit frontend:
   ```bash
    streamlit run ui/main.py
    ```
3. Open your browser and navigate to `http://localhost:8501` to access the Streamlit interface.
4. Use the interface to input transaction data and receive predictions on whether the transaction is anomalous.