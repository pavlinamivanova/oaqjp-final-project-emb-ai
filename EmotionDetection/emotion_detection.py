import requests, json
def emotion_detector(text_to_analyse): 
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    
    data = json.loads(response.text)
	# Extracting sentiment label and score from the response
    emotion_list ={}
    emotion_list["anger"]= data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("anger")
    emotion_list["disgust"]= data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("disgust")
    emotion_list["fear"]= data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("fear")
    emotion_list["joy"]= data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("joy")
    emotion_list["sadness"] = data.get("emotionPredictions", [{}])[0].get("emotion", {}).get("sadness")
    res="" 
    emo_max=""
    emo_val=0
    for key, value in emotion_list.items():
        res+=("{}: {} , ".format(key, value))
        if value>emo_val:
            emo_val=value
            emo_max=key
    
    emotion_list["dominant_emotion"]= emo_max
    res+= "dominant_emotion: "+ emotion_list["dominant_emotion"] 
           
    return {res}

    