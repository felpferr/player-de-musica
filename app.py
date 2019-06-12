from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
@app.route('/<nome>')
def main(nome="mundo"):
    l = ["maca", "banana", "goiaba"]
    return render_template("index.html", nome=nome, lista=l)

@app.route('/ola')
@app.route('/ola/<nome>')
def ola(nome="mundo"):
    return 'ola ' + nome

if __name__ == "__main__":
    app.run(debug=True)