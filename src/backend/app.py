from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/citizen-science")
db = mongodb_client.db

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/api/v1/questions', methods=['GET'])
def getQuestions():
    cursor = db.question.find_one({"used":0})
    if cursor is None:
        return "Questions expired"
    new_values = { "$set": { "used": 1 } }
    db.question.update_one(cursor,new_values)
    return cursor["question_list"]
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
