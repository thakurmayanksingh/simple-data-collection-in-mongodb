from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")

db = client['learning']
collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get("age")

        if name and age:
            collection.insert_one({"name": name, "age": age})
            return redirect('/')
        
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)