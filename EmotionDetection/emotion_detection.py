import requests

def emotion_predictor(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    if not text_to_analyze or text_to_analyze.strip() == '':
        raise ValueError("Input text is blank. Pleases provide valid text for analysis.")

    data= {
        "raw_document": {
        "text" : text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 400:
        return None, None
    
    response.raise_for_status()

    formatted_response = response.json()

    emotions=formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]

    return dominant_emotion, dominant_score

#emotion_predictor("I love new technology")

try: 
    print(emotion_predictor("I love new technology"))
    print(emotion_predictor(""))
except Exception as e:
    print(f"Error : {e}") 




