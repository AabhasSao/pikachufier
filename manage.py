from flask import Flask, render_template, request
from pika import pikachufier

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', the_title = "Let's get pikachufied.")

@app.route('/results', methods = ['POST',])
def pikachufy():
    name = request.form['user_name']
    result = pikachufier(name)
    return render_template('results.html', name_pikachufied = result,
    the_title = "Results", the_name = name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
