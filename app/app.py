from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
mongo_uri = "mongodb+srv://TEPIS:TEPIS355@cluster0.lu5p4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client['TEPIS']


@app.route('/')
def hello_world():
    try:
        client.admin.command('ping')
        return 'MongoDB Connection Successful!'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)