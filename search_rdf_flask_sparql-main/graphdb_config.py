from graphdb.rdf4j.api.sparql_api import SparqlApi
from graphdb.rdf4j.configuration import Configuration
from graphdb.rdf4j.api_client import ApiClient

conf = Configuration()
conf.host = "http://localhost:8000/"
api = SparqlApi(ApiClient(configuration=conf))
repository = "kde_test"