#!/usr/bin/env python

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def guess_result():
    guess = int(request.form['index'])
    if guess == 7:
        return redirect('/correct')
    else:
        return redirect('/incorrect')

@app.route('/correct')
def correct():
    return render_template('correct.html')

@app.route('/incorrect')
def incorrect():
    return render_template('incorrect.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
