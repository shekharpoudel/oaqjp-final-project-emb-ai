import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function that takes a string input 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    inputjson = { "raw_document": { "text": text_to_analyse }}  # Create a dictionary with the text to be analyzed
    response = requests.post(url, json = inputjson, headers=header)  # Send a POST request to the API with the text and headers
    #for error handling return all None
    if response.status_code == 400:
            return { 'anger': None,  'disgust': None,  'fear': None, 'joy': None, 
                'sadness': None, 'dominant_emotion': None}
    
    dictdata = json.loads(response.text) #convert to dict
    emotions = dictdata['emotionPredictions'][0]['emotion'] #get emotions data
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)    
    return {
        'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }# Return formatted output