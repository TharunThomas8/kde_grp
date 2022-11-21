import os
import queries
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method =='GET':
        return render_template("index.html", showtable=0)
    else:   
        question = request.form.get("question")
        match question: 
            case 'q1': 
                query_result = queries.q1_result
            case 'q2':
                query_result = queries.q1_result
            case 'q3':
                print('No match found')
            case 'q4':
                print('No match found')
        return render_template("index.html", query_result = query_result, showtable=1 )

if __name__ == "__main__":
    app.run()
