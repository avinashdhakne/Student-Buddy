from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
   
    
@app.route('/grammar', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        text = request.form['video_url']
        correct_grammar = correct_grammar(text)
        print("---->>>", correct_grammar)
        return render_template('grammar.html', thumbnail_url=correct_grammar)
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

if __name__ == '__main__':
    app.run(debug=True)