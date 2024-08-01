import json

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""
配置自己的 阿里云 url api_key 这里的是不可用的
"""
url = ""
api_key = ""


def chat_ali(a_msg: str) -> str:
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": "qwen2-72b-instruct",
        "input": {
            "messages": [
                {"role": "system", "content": ""},
                {"role": "user", "content": a_msg},
            ],
        },
        "parameters": {},
    }
    try:
        resp = requests.post(url, headers=headers, json=data)
        data = resp.content.decode("utf-8")
        jer = json.loads(data)
        text = jer["output"]["text"]
        with open("aaa.json", "w", encoding="utf-8") as f:
            json.dump(jer, f, ensure_ascii=False, indent=4)
        return text
    except Exception as e:
        print(e)
    return ""


@app.post("/chat")
def chat():
    try:
        jer = json.loads(request.data)
        msg = jer["msg1"]
        ack = chat_ali(msg)
        return jsonify({"ack": ack})
    except json.JSONDecodeError:
        return "Invalid JSON data", 400


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
