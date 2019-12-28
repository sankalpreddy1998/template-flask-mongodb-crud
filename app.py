from flask import *
from flask_pymongo import PyMongo
import flask_json
import numpy
from bson.objectid import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'my_db_name'
app.config['MONGO_URI'] = 'mongodb://localhost/my_db_name'

mongo = PyMongo(app)

@app.route("/data",methods=['GET'])
def get_data():
    data=[]
    task = mongo.db.my_collection_names
    cursor = task.find({})
    for i in cursor:
        dict={'_id':str(i['_id']),'task':i['task']}
        data.append(dict)
    return jsonify({"data":data})


@app.route("/",methods=['POST'])
def post():
    task = mongo.db.my_collection_names
    req_data = request.get_json()
    a=req_data['task']
    print(a)
    task.insert({"task":a})
    return "success"

@app.route("/",methods=['GET'])
def get():
    return render_template("home.html")

@app.route("/",methods=['DELETE'])
def delete():
    id=request.args.get('_id')
    task = mongo.db.my_collection_names
    x=task.delete_many({"_id":ObjectId(id)})
    return "success"


@app.route("/",methods=['PUT'])
def update():
    id=request.args.get('_id')
    print(id)
    req_data = request.get_json()
    a=req_data['task']
    print(a)
    task = mongo.db.my_collection_names
    x=task.find_one({"_id":ObjectId(id)})
    print(x)
    x['task']= a
    task.save(x)
    return "success"

if __name__ == "__main__":
   app.run(debug=True)
