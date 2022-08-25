import json,os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/citizen-science")
db = mongodb_client.db

sibB = os.path.join(os.path.dirname(__file__), 'Flask-Server')
json_file = open("src/backend/data/question_list.json")
question_data = json.load(json_file)
for i in range(0,50):
    db_list = []
    temp_list = question_data[str(i)]
    temp_list.sort()
    for question in temp_list:
        db_list.append("QID"+str(question))

    db.question.insert_one({"question_list": db_list, "used":0})


cursor = db.question.find_one({"used":0})
print(cursor)