import os   # This is to gain access to the environ variables below
from flask import (Flask,   # This is for flask.
    flash, render_template, # Render_template is how to build the base/template version of websites
     redirect, request, session, url_for)
from flask_pymongo import PyMongo   # This is used to manipulate mongo with python
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
