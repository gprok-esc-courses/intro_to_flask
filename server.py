from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/api/data")
def api_data():
    return jsonify({'users': ['john', 'peter', 'mike']})

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/news")
def news():
    news_items = ['Opened new store', 'Cooperation with MagicCo', 'Raised $1M funding']
    return render_template('news.html', news=news_items)