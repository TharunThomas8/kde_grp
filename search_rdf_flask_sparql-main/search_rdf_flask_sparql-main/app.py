from flask import Flask,render_template,request
import os
from graphdb.rdf4j.api.sparql_api import SparqlApi
from graphdb.rdf4j.configuration import Configuration
from graphdb.rdf4j.api_client import ApiClient

conf = Configuration()
conf.host = "http://localhost:8000/"
api = SparqlApi(ApiClient(configuration=conf))
repository = "kde_test"

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method =='GET':
        return render_template("index.html", showtable=0)
    else:  
        q1_result = api.execute_get_select_query(repository, """prefix ex: <http://data.example.org/ont>
        prefix foaf: <http://xmlns.com/foaf/0.1/>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix ont: <http://data.example.org/bus/77a/>
        prefix loca1: <http://data.example.org/stop/822GA00278/>
        prefix loca2: <http://data.example.org/stop/822GA00467/>
        prefix geo: <http://www.opengis.net/ont/geosparql#>
        PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
        PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>

        select ?loc1 ?loc2 where { 
            loca1:loc geo:hasGeometry ?loc1 .
            loca2:loc geo:hasGeometry ?loc2 .
            # BIND(round(geof:distance(?loc1,?loc2, uom:metre)) 
                # AS ?res)
        }""", _return_http_data_only=True)
            
        question = request.form.get("question")
        match question: 
            case 'q1': 
                query_result = q1_result
            case 'q2':
                query_result = q1_result
            case 'q3':
                print('No match found')
            case 'q4':
                print('No match found')

        return render_template("index.html", query_result = query_result, showtable=1 )


if __name__ == "__main__":
    app.run(debug=True)
