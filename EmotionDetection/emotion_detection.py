import requests, json
def emotion_detector(text_to_analyse): 
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    
    data = json.loads(response.text)
    emotion_list ={}
    if response.status_code == 200:
        emotion_list["anger"]= data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("anger")
        emotion_list["disgust"]= data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("disgust")
        emotion_list["fear"]= data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("fear")
        emotion_list["joy"]= data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("joy")
        emotion_list["sadness"] = data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("sadness")
        emo_max=""
        emo_val=0
        for key, value in emotion_list.items():
            if value>emo_val:
             emo_val=value
             emo_max=key
        emotion_list["dominant_emotion"]= emo_max

    elif response.status_code == 400:
        emotion_list["anger"]=None
        emotion_list["disgust"]=None
        emotion_list["fear"]=None
        emotion_list["joy"]=None
        emotion_list["sadness"]=None
        emotion_list["dominant_emotion"]=None
    return emotion_list

    