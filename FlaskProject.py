from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'Contact': '9987644456',
        'Name': 'Raju',
        'Done': False, 
        'ID': 1
    },
    {
        'Contact': '9876543222',
        'Name': 'Rahul',
        'Done': False, 
        'ID': 2
    }
]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status" : "Error",
            "message" : "Please provide the data!"
        },400)

    task = {
        'Contact' : request.json.get('Contact', ""),
        'Name' : request.json['Name'],
        'ID' : data[-1]['ID'] + 1,
        'done' : False
    }
    data.append(task)
    return jsonify({
        "status" : "Success",
        "message" : "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)