from flask import Flask, url_for, request
from markupsafe import escape
import time
app = Flask(__name__)

data= {
        "door1": "OFF",
        "door2": "OFF",
        }

@app.route("/condition")
def condition_api():
    
    return data

@app.route("/", methods=['GET'])
def change_data():
    
    data['door1'] = request.args.get('door1')
    data['door2'] = request.args.get('door2')
    
    #Если получил ON на замок, то открыть замок на 5 секунд, затем поставить OFF
    if data["door1"]=="ON":
        print(data)
        time.sleep(5)
            
        data["door1"]="OFF"

        time.sleep(5)
        print(data)
        
    if data["door1"]=="ON":
        print(data)
        time.sleep(5)
            
        data["door1"]="OFF"

        time.sleep(5)
        print(data)
        
        
    return data
#request.args.get('door1', '')

app.run(host='localhost', port=4568)
