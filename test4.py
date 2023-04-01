# importing Flask and other modules
from flask import Flask, request, render_template

from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://juhi:juhi@mpr.ioawzd0.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('my_database')

# Flask constructor
app = Flask(__name__)

def test(myname):
    print('request')
    db.mpr_database.insert_one(myname)
    return "Success"

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def flask_mongodb_atlas():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        ans1 = request.form.get("ans1")
        test({"first_name":first_name,
              "last_name":last_name,
              "Image":ans1})
        return "Success"
    return render_template("form.html")



if __name__=='__main__':
    app.run()
