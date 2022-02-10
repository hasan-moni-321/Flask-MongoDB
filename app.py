from typing import final
from flask import Flask, redirect, render_template, request, url_for 

import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

app = Flask(__name__) 
 
try: 
    mydb = myclient["mydatabase30"]
    mycol = mydb["customers30"] 
    print("database and collection has created ") 
except: 
    print('database and collection has not created')


@app.route('/') 
def home(): 
    return render_template('student.html') 


@app.route('/result', methods=['POST', 'GET']) 
def result(): 
    if request.method == 'POST': 
        name = request.form['name'] 
        id = request.form['id']
        address = request.form['address']

        try: 
            data_dict = {'name': name, 'id': id, 'address': address}  
            mycol.insert_one(data_dict) 
            msg = 'data inserted'
        except: 
            msg = 'data not inserted' 
        finally:
            return render_template('result.html', msg = msg)


if __name__ == '__main__': 
    app.run(debug=True) 
    