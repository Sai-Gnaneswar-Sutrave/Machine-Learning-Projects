# Insurance Premium Category Predictor

This project is a machine learning application that predicts the insurance premium category for individuals based on their demographic and health-related information. The model is trained on a dataset containing various features such as age, gender, BMI, smoking status, and more. The API is built using FastAPI and provides endpoints for making predictions, checking the health of the API, and a home endpoint to verify that the API is running.

## Features
- Predict insurance premium category based on user input
- Health check endpoint to monitor the status of the API
- Home endpoint to verify that the API is running
- Model versioning for better maintenance and updates

## Technologies Used
- Python
- FastAPI
- scikit-learn

## Installation
1. Clone the repository:
   ```bash
   git clone
    ```
2. Navigate to the project directory:
    ```bash
    cd Insurance-Premium-Category-Predictor
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```       

## Usage
1. Start the FastAPI server:
    ```bash
    uvicorn app:app --reload
    ```
2. Access the API documentation at `http://localhost:8000/docs` to test the endpoints. 
3. Use the `/predict` endpoint to get predictions for insurance premium categories based on user input.
4. Use the `/health` endpoint to check the health status of the API.
5. Use the `/` endpoint to verify that the API is running.