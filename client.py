import requests
import json

api_key = "AIzaSyAPqgQ7F3xD0PbRb20C5siOxrrhF7UkjcQ"
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [{
        "parts": [{
            "text": "Explain recursion in simple words."
        }]
    }]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    print(data['candidates'][0]['content']['parts'][0]['text']) 
else:
    print(f"Error: {response.status_code}")
    print(response.text)