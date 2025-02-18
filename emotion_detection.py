
import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/analyze"  # Ensure this is the correct URL
    myobj = {"raw_document": {"text": text_to_analyse}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_v1"}  # Ensure correct model ID

    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()  # Raises an error for HTTP 4xx/5xx responses
        return response.json()  # Return JSON data instead of raw text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Run the function and print output for GitHub Actions
if __name__ == "__main__":
    test_text = "I am feeling very happy today!"
    result = emotion_detector(test_text)
    print("Emotion Detection Output:", result)
