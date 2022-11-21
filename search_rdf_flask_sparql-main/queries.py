from graphdb_config import api, repository

q1_result = api.execute_get_select_query(repository, """
        prefix ex: <http://data.example.org/ont>
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