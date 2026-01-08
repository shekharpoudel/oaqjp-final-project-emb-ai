import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function that takes a string input 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    inputjson = { "raw_document": { "text": text_to_analyse }}  # Create a dictionary with the text to be analyzed
    response = requests.post(url, json = inputjson, headers=header)  # Send a POST request to the API with the text and headers
    return response.text  # Return the response text from the API
 
