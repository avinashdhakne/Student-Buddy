from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

# text summarization
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        thumbnail_url = generate_thumbnail(video_url)
        print("---->>>", thumbnail_url)
        return render_template('index.html', thumbnail_url=thumbnail_url)
    else:
        return render_template('index.html')

def generate_thumbnail(video_url):
    api_url = "https://v1.genr.ai/api/circuit-element/summarize"
    response = requests.post(api_url, json={ "text":video_url,"temperature": 0,"max_words": 15})
    if response.status_code == 200:
        return json.loads(response.text)["output"]
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)