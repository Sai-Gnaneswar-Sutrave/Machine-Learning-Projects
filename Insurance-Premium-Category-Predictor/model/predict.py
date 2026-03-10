import pickle
import pandas as pd


# Import the model
with open(r'./model/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
# MLFlow version
MODEL_VERSION = '1.0.0'

# Class labels from the model
class_labels = model.classes_.tolist()

def predict_premium_category(user_input: dict) -> str:
    
    '''
    This function takes the input data, processes it, and returns the predicted insurance premium category.
    '''
    
    input_data = pd.DataFrame([user_input])

    # Predict the class label using the loaded model
    predicted_class = model.predict(input_data)[0]

    # Get the probabilities for all classes
    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities)

    # Create mapping of class labels to their corresponding probabilities
    class_probabilities = dict(zip(class_labels, map(lambda x: round(x, 4), probabilities)))

    return {
        "predicted_class": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probabilities
    }