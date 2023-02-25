from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index1.html')
    
@app.route('/grammar', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        text = request.form['video_url']
        grammar_txt = correct_grammar(text)
        print("---->>>", grammar_txt)
        return render_template('grammar.html', thumbnail_url=grammar_txt)
    else:
        return render_template('grammar.html')
    

def correct_grammar(input_para):
    api_url = "https://v1.genr.ai/api/circuit-element/correct-grammar"
    parameters = {
    "text": input_para,
    "temperature": 0,
    }
    response = requests.post(api_url, json=parameters)
    if response.status_code == 200:
        return json.loads(response.text)["output"]
    else:
        return None
    
@app.route('/summarize', methods=['GET', 'POST'])
def index3():
    if request.method == 'POST':
        text = request.form['video_url']
        correct_grammar = summarize(text)
        print("---->>>", correct_grammar)
        return render_template('summarize.html', thumbnail_url=correct_grammar)
    else:
        return render_template('summarize.html')

def summarize(input_para):
    api_url = "https://v1.genr.ai/api/circuit-element/summarize"
    parameters = {
    "text": input_para,
    "temperature": 0,
    "max_words": 15
    }
    response = requests.post(api_url, json=parameters)
    if response.status_code == 200:
        return json.loads(response.text)["output"]
    else:
        return None
    
@app.route('/visualize', methods=['GET', 'POST'])
def index4():
    if request.method == 'POST':
        text = request.form['video_url']
        correct_grammar = generate_prompt(text)
        print("---->>>", correct_grammar)
        return render_template('visualize.html', thumbnail_url=correct_grammar)
    else:
        return render_template('visualize.html')
    

def generate_prompt(input_para):
    api_url = "https://v1.genr.ai/api/circuit-element/generate-prompt"
    parameters = {
    "text": input_para,
    "temperature": 0,
    }
    print("------>>> prompt generated\n")
    response = requests.post(api_url, json=parameters)
    if response.status_code == 200:
        return generate_image(json.loads(response.text)["output"])
    else:
        return None
    
    
def generate_image(input_para):
    api_url = "https://v1.genr.ai/api/circuit-element/generate-image"
    parameters = {
        "prompt": input_para,
        "height": 512,
        "width": 512,
        "model": "stable-diffusion-2",
        "n_images": 1
    }
    print("------>>> image generated\n")
    response = requests.post(api_url, json=parameters)
    if response.status_code == 200:
        return json.loads(response.text)["output"]
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)