#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import Twython
from flask import Flask, Response, json


#Flask app
app = Flask(__name__)


@app.route("/")
def init():

	#Get tweets by term
	results = getStream('Pisco Sour', 1000)
	#Returns a json format
	json = formatStream(results)	

	#Prin values in json, ready to use in javascript
	return Response(json,  mimetype='application/json')


#Setup to get Tweets
def setupStream( ):

	t = Twython(app_key='pTb3Yt82eTfa29l7P6HuHYGPh', 
	            app_secret='Ac9AIOOa0DrfJNZFQEPlkilqYIPTSCqpoUmWcbXppE5dKpWjWi', 
	            oauth_token='64845117-SNcgxtWaRJ4rbgnpWquLPicaL8vW6iA7U1qCUkxsw', 
	            oauth_token_secret='hVCkPcMCXZfiM7lFmErDkTqgqC2pANTij93zpLXOoqAnQ')
	return t


#Returns tweets, we can add more functions, filters, etc.
def getStream(term, count):
	t = setupStream()
	#&src=typd
	result = t.search(q=term, count=count)
	return result


#Format and values to return
def formatStream(results):

	tweets = []	
	for t in results['statuses']:
		tweets.append(t)
  	return json.dumps(tweets)


#Init the app
if __name__ == '__main__':

	#Active debug
	app.debug = True

	app.run(host='0.0.0.0')