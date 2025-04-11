from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/garbage_reminder", methods=["POST"])
def reminder():
    response_url = request.form.get("response_url")

    message = {
        "response_type": "in_channel",
        "text": """----------------Japanese---------------------
😎ごみ当番についてのリマインダー...
・ロッカーの紙に従って行ってくれ・・・（シュレッダーやペットボトルのごみなどお忘れなく！）
・その日が無理な場合はこのチャンネルで代わりに出られる人を募ってくれ・・・
・当番を終えたらこのチャンネルで通知してくれ・・・

----------------English---------------------
Garbage Duty Reminder 😎
・Please follow the locker instructions (don’t forget shredder waste or PET bottles!)
・If you can't take your shift, please ask in this channel
・Notify the channel once you’re done with your duty!
"""
    }

    # Slackに返信を送信
    requests.post(response_url, json=message)
    return "Reminder sent!"

@app.route("/", methods=["GET"])
def home():
    return "Garbage Reminder Bot is alive!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
