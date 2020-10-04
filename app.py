from flask import Flask, request, redirect, url_for, render_template
from flask_restful import Api, Resource
import common

app = Flask(__name__)
api = Api(app)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html', mappingTable=common.MAPPING_TABLE)

@app.route("/api/replace", methods=['GET','POST'])
def api():
    if request.method == 'POST' and len(request.form['replace']) > 0 :
        stringToReplace = request.form['replace']
        result = {
            "data": {
                "Provided String" : stringToReplace,
                "Replaced String" : common.replaceAll(stringToReplace)
            }
        }
        mylist = f"{result}"
        return (render_template('output.html',output=result),result)
    else:
        return redirect(url_for('home'))