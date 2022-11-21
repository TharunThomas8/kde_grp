

q1_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?busStopName1 ?busStopName2 ?busName1 where {
    {
    select ?busStopName1 ?seqName1 ?busName1 ?dis1 where {

        ?prop foaf:name "34 NAAS RD, BLUEBELL, DUBLIN, Dublin, Ireland" .
        ?prop ex:hasLocation  ?propLoc .
        ?propLoc geo:hasGeometry ?apartLatLong .

        ?bus rdf:type ex:Bus .
        ?bus ex:hasBusTrip ?trip ;
             foaf:name ?busName1 .
        ?trip ex:hasBusStopSequenceNumber ?seq1 .
        ?seq1 ex:hasBusStop ?stop ;
              foaf:name ?seqName1 .
        ?stop ex:hasLocation ?loc ;
              foaf:name ?busStopName1 .
        ?loc geo:hasGeometry ?buslatlong .

        BIND(round(geof:distance(?buslatlong,?apartLatLong, uom:metre)) AS ?dis1) .
#            FILTER(?dist1 < 1000)
		}
        ORDER BY ASC(?dis1)
#        LIMIT 10
    }
    {
    select ?busStopName2 ?seqName2 ?busName2 ?dis2 where {
#        ?club rdf:type ex:RecreationClub .
        ?club foaf:name "Killinarden, Tallaght, Dublin 24" .
        ?club ex:hasLocation ?clubLoc .
        ?clubLoc geo:hasGeometry ?clubLatLong .

        ?bus rdf:type ex:Bus ;
             foaf:name ?busName2 .
        ?bus ex:hasBusTrip ?trip .
        ?trip ex:hasBusStopSequenceNumber ?seq2 .
        ?seq2 ex:hasBusStop ?stop ;
              foaf:name ?seqName2 .
        ?stop ex:hasLocation ?loc ;
              foaf:name ?busStopName2 .
        ?loc geo:hasGeometry ?buslatlong .

        BIND(round(geof:distance(?buslatlong,?clubLatLong, uom:metre)) AS ?dis2) .
#        FILTER(?dist2 < 1000)
		}
        ORDER BY ASC(?dis2)
#        LIMIT 10
    }
    
    FILTER(?busName1 = ?busName2) .
    FILTER(xsd:integer(?seqName1) < xsd:integer(?seqName2)) .
#    
    

}
LIMIT 10
"""

q2_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#prefix ont: <http://data.example.org/bus/77a/>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?dis ?prop where {
    
    ?prop foaf:name "34 NAAS RD, BLUEBELL, DUBLIN, Dublin, Ireland" .
        ?prop ex:hasLocation  ?propLoc .
        ?propLoc geo:hasGeometry ?apartLatLong .
    
    ?sportsClub  rdf:type ex:SportsClub .
    ?sportsClub ex:hasAddress ?sportsAdd .
    ?sportsAdd ex:hasLocation ?sportsLoc .
    ?sportsLoc geo:hasGeometry ?sportsLatLong
    
    BIND(round(geof:distance(?apartLatLong,?sportsLatLong, uom:metre)) AS ?dis) .
}
ORDER BY ASC(?dis)
LIMIT 3
"""

q3_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#prefix ont: <http://data.example.org/bus/77a/>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?busStopName ?dis1 ?luasStopName ?dis2 where {
    
    ?club foaf:name "Killinarden, Tallaght, Dublin 24" .
        ?club ex:hasLocation ?clubLoc .
        ?clubLoc geo:hasGeometry ?clubLatLong .
    
    ?bus rdf:type ex:Bus .
        ?bus ex:hasBusTrip ?trip1 ;
             foaf:name ?busName1 .
        ?trip ex:hasBusStopSequenceNumber ?seq1 .
        ?seq1 ex:hasBusStop ?stop ;
              foaf:name ?seqName1 .
        ?stop ex:hasLocation ?loc ;
              foaf:name ?busStopName .
        ?loc geo:hasGeometry ?buslatlong .
    
    ?luas rdf:type ex:Luas .
        ?luas ex:hasLuasTrip ?trip2 ;
             foaf:name ?luasName2 .
        ?trip2 ex:hasLuasStopSequenceNumber ?seq2 .
        ?seq2 ex:hasLuasStop ?stop2 ;
              foaf:name ?seqName2 .
        ?stop2 ex:hasLocation ?loc2 ;
              foaf:name ?luasStopName .
        ?loc2 geo:hasGeometry ?luaslatlong .
    
    
    BIND(round(geof:distance(?clubLatLong,?buslatlong, uom:metre)) AS ?dis1) .
    BIND(round(geof:distance(?clubLatLong,?luaslatlong, uom:metre)) AS ?dis2) .
}
ORDER BY ASC(?dis1) ASC(?dis2)
LIMIT 3
"""

q4_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#prefix ont: <http://data.example.org/bus/77a/>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?clubname ?dis1 where {
    
        ?club rdf:type ex:SportsClub .
    	?club foaf:name ?clubname .
    	?club ex:hasAddress ?clubAdd .
        ?clubLoc ex:isLocationOf ?clubAdd .
        ?clubLoc geo:hasGeometry ?clubLatLong .

        ?stop foaf:name "Ringsend Road, stop 395" .
    	?loc ex:isLocationOf ?stop  .
        ?loc geo:hasGeometry ?stoplatlong .

    BIND(round(geof:distance(?clubLatLong,?stoplatlong, uom:metre)) AS ?dis1) .
}
ORDER BY ASC(?dis1)
LIMIT 3
"""

q5_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix bus: <http://data.example.org/bus/13/>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
#PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

#select ?seq where {
select ?clubName (SAMPLE(?busStopName) AS ?busStopName) (SAMPLE(?dis) AS ?dis) where{
    ?club rdf:type ex:SportsClub .
    ?club ex:hasAddress ?clubAdd .
    ?clubloc ex:isLocationOf ?clubAdd .
    ?club foaf:name ?clubName .
    ?clubloc geo:hasGeometry ?clublatlong .
#    
#    loca2:loc geo:hasGeometry ?loc2 .
#     
    
    bus:1 ex:hasBusStopSequenceNumber ?seq .
    ?seq ex:hasBusStop ?busStop .
    ?busLoc ex:isLocationOf ?busStop .
#          foaf:Name ?busStopName .
    ?busLoc geo:hasGeometry ?buslatlong .
#    ?busTrip ex:isOnBusTrip  .
#    bus:1 ex:isBusTripOf ?bus .
#    ?bus foaf:name ?
    ?busStop foaf:name ?busStopName .
    
    BIND(round(geof:distance(?clublatlong,?buslatlong, uom:metre)) AS ?dis) .
    
#    FILTER(?dis < 2000)
    
}
GROUP BY ?clubName
ORDER BY ASC(?dis)
LIMIT 5
"""

q6_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?recName where {
    	?prop foaf:name "34 NAAS RD, BLUEBELL, DUBLIN, Dublin, Ireland" .
        ?prop ex:hasLocation  ?propLoc .
        ?propLoc geo:hasGeometry ?apartLatLong .
    
        ?recClub rdf:type ex:RecreationClub .
    	?recClub ex:hasFacilities ?recFac ;
              	foaf:name ?recName .
    	?recFac ex:hall ?recHall .
    	?recClub ex:hasAddress ?recAdd .
    	?recAdd ex:hasLocation ?recLoc .
    	?recLoc geo:hasGeometry ?recLatLong .
    	FILTER (?recHall = "Yes")
    
    	BIND(round(geof:distance(?buslatlong,?apartLatLong, uom:metre)) AS ?dis1) .
   }
ORDER BY ASC(?dis1)
        LIMIT 10


"""

q7_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?recName where {
    	?prop foaf:name "34 NAAS RD, BLUEBELL, DUBLIN, Dublin, Ireland" .
        ?prop ex:hasLocation  ?propLoc .
        ?propLoc geo:hasGeometry ?apartLatLong .
    
        ?recClub rdf:type ex:RecreationClub .
    	?recClub ex:hasFacilities ?recFac ;
              	foaf:name ?recName .
    	?recFac ex:hall ?recHall .
    	?recClub ex:hasAddress ?recAdd .
    	?recAdd ex:hasLocation ?recLoc .
    	?recLoc geo:hasGeometry ?recLatLong .
    	FILTER (?recHall = "Yes")
    
    	BIND(round(geof:distance(?buslatlong,?apartLatLong, uom:metre)) AS ?dis1) .
   }
ORDER BY ASC(?dis1)
        LIMIT 10


"""

q8_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?recName where {
    	?prop foaf:name "34 NAAS RD, BLUEBELL, DUBLIN, Dublin, Ireland" .
        ?prop ex:hasLocation  ?propLoc .
        ?propLoc geo:hasGeometry ?apartLatLong .
    
        ?recClub rdf:type ex:RecreationClub .
    	?recClub ex:hasFacilities ?recFac ;
              	foaf:name ?recName .
    	?recFac ex:hall ?recHall .
    	?recClub ex:hasAddress ?recAdd .
    	?recAdd ex:hasLocation ?recLoc .
    	?recLoc geo:hasGeometry ?recLatLong .
    	FILTER (?recHall = "Yes")
    
    	BIND(round(geof:distance(?buslatlong,?apartLatLong, uom:metre)) AS ?dis1) .
   }
ORDER BY ASC(?dis1)
        LIMIT 10
"""

q9_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?recName where {
    	?prop foaf:name "34 NAAS RD, BLUEBELL, DUBLIN, Dublin, Ireland" .
        ?prop ex:hasLocation  ?propLoc .
        ?propLoc geo:hasGeometry ?apartLatLong .
    
        ?recClub rdf:type ex:RecreationClub .
    	?recClub ex:hasFacilities ?recFac ;
              	foaf:name ?recName .
    	?recFac ex:hall ?recHall .
    	?recClub ex:hasAddress ?recAdd .
    	?recAdd ex:hasLocation ?recLoc .
    	?recLoc geo:hasGeometry ?recLatLong .
    	FILTER (?recHall = "Yes")
    
    	BIND(round(geof:distance(?buslatlong,?apartLatLong, uom:metre)) AS ?dis1) .
   }
ORDER BY ASC(?dis1)
        LIMIT 10
"""

q10_query = """
prefix ex: <http://data.example.org/ont#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix loca1: <http://data.example.org/stop/8240DB000324/>
prefix loca2: <http://data.example.org/stop/8220DB004521/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:  <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX bus: <http://data.example.org/bus/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?recName ?sportsName where {
    
        ?recClub rdf:type ex:RecreationClub .
    	?recClub ex:hasAddress ?recAdd ;
    			foaf:name ?recName .
    	?recAdd ex:hasLocation ?recLoc .
    	?recLoc geo:hasGeometry ?recLatLong .
    
    	?sportsClub rdf:type ex:SportsClub .
    	?sportsClub ex:hasAddress ?sportsAdd ;
                 foaf:name ?sportsName .
    	?sportsAdd ex:hasLocation ?sportsLoc .
    	?sportsLoc geo:hasGeometry ?sportsLatLong .
    
    	BIND(round(geof:distance(?sportsLatLong,?recLatLong, uom:metre)) AS ?dis1) .
   }
ORDER BY ASC(?dis1)
    LIMIT 10
"""