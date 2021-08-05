import os
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
  return render_template('index.html')

@app.route('/api/')
def all_data():
  response = {
    "bugsnax": "https://bugsnaxapi.com/api/bugsnax",
    "locations": "https://bugsnaxapi.com/api/locations",
    "grumpuses": "https://bugsnaxapi.com/api/grumpuses",
  }

  return jsonify(response)

@app.route('/api/bugsnax/')
def bugsnax_root():
  with open('data/bugsnax.json') as f:
    data = json.load(f)

  return {"bugsnax": data}

@app.route('/api/bugsnax/<index>/')
def bugsnax_endpoint(index):
  with open('data/bugsnax.json') as f:
    data = json.load(f)

  if index.isdigit():
    if int(index) > len(data):
      return "Error: Invalid index"
    return data[int(index)+1]
  else:
    for i in data:
      if i['name'].lower().replace(" ", "") == index.lower().replace(" ", "").replace("-", ""):
        return i

  return "Error: Invalid name"

@app.route('/api/locations/')
def locations_root():
  with open('data/locations.json') as f:
    data = json.load(f)

  return {"locations": data}

@app.route('/api/locations/<index>/')
def locations_endpoint(index):
  with open('data/locations.json') as f:
    data = json.load(f)

  if index.isdigit():
    if int(index) > len(data):
      return "Error: Invalid index"
    return data[int(index)+1]
  else:
    for i in data:
      print(i)
      print(index)
      if i['name'].lower().replace(" ", "") == index.lower().replace(" ", "").replace("-", ""):
        return i

  return "Error: Invalid name"

@app.route('/api/grumpuses/')
def grumpuses_root():
  with open('data/grumpuses.json') as f:
    data = json.load(f)

  return {"grumpuses": data}

@app.route('/api/grumpuses/<index>/')
def grumpuses_endpoint(index):
  with open('data/grumpuses.json') as f:
    data = json.load(f)

  if index.isdigit():
    if int(index) > len(data):
      return "Error: Invalid index"
    return data[int(index)+1]
  else:
    for i in data:
      if i['name'].lower().replace(" ", "") == index.lower().replace(" ", "").replace("-", ""):
        return i

  return "Error: Invalid name"

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))