import sys
from flask import Flask, render_template
app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    return app

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", status_code=200, poem="The Symphony of Software: A Tribute to Digital Innovation", author="Bard")

@app.route('/bugs', methods=['GET'])
def bug():
    return render_template("bugs.html", status_code=200, poem="“The Developer’s Struggle: A Tale of Code and Resilience”", author="Bard")

@app.route('/mindset', methods=['GET'])
def mindset():
    return render_template("mindset.html", status_code=200, poem="The Dance of Code: A Developer's Journey", author="Bard")

@app.route('/teamwork', methods=['GET'])
def teamwork():
    return render_template("teamwork.html", status_code=200, poem="Software Development, A Tale of Teamwork", author="Bard")

if __name__ == "__main__":
    app.run(debug=True)