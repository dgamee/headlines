from turtle import title
from webbrowser import get
import feedparser

from flask import Flask,render_template,request
app = Flask(__name__)

rss_feed = {
    'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640',
    'football' : 'https://www.101greatgoals.com/feed/'  }

@app.route('/')
def bbc():
    return get_news('bbc')

@app.route('/football')
def football_feed():
    return get_news('football')

@app.route('/fox')
def fox():
    return get_news('fox')

@app.route('/iol')
def iol():
    return get_news('iol')

@app.route('/cnn')
def cnn():
    return get_news('cnn')

def get_news(site):
    feed = feedparser.parse(rss_feed[site])
    first_article = feed['entries'][0]
    return render_template('index.html', articles = feed['entries'])
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)