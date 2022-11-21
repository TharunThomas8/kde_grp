import os
import queries
from graphdb_config import api, repository
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
                the_query = queries.q1_query
            case 'q2':
                the_query = queries.q2_query
            case 'q3':
                the_query = queries.q3_query
            case 'q4':
                the_query = queries.q4_query
            case 'q5':
                the_query = queries.q5_query
            case 'q6':
                the_query = queries.q6_query
            case 'q7':
                the_query = queries.q7_query
        query_result = api.execute_get_select_query(repository, the_query , _return_http_data_only=True)
        return render_template("index.html", query_result = query_result, showtable=1 )

if __name__ == "__main__":
    app.run()
