from flask import Flask,jsonify,request

app=Flask(__name__)

#creating a array of tasks with eachtask as a different object in it
tasks=[
    {
        'Contact': "8473948838",
        'Name': "John",
        'done':False,
        'id': 1



    },
    {

        'id': 2,
        'Name': "Rahul",
        "Contact": '8392403942',
        'done': False



    }
]


@app.route('/add-data',methods=["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    })     


if (__name__ == "__main__"):
    app.run(debug=True)    