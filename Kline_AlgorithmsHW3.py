def geojsondict(filein):
    import json, pprint
    indata = open(filein,"r")
    jsonstr = indata.read()
    geodict = json.loads(jsonstr)
    accumulator = 0
    while len(geodict['features']) > accumulator:
        features = geodict["features"][accumulator]
        print("State name: {0:6s}".format(features["properties"]["STATE_NAME"]))
        print("Area:       {0:6f}".format(features["properties"]["Area"]))
        print("State FIPS: {0:1d}".format(features["properties"]["STATE_FIPS"]))
        coords = features["geometry"]["coordinates"]
        minlat = 99999
        maxlat = -99999
        minlong = 99999
        maxlong = -99999
        accumulator2 = 0
        while accumulator2 < len(coords[0]):
            if coords[0][accumulator2][0] < minlong:
                minlong = coords[0][accumulator2][0]
            if coords[0][accumulator2][0] > maxlong:
                maxlong = coords[0][accumulator2][0]
            if coords[0][accumulator2][1] < minlat:
                minlat = coords[0][accumulator2][1]
            if coords[0][accumulator2][1] > maxlat:
                maxlat = coords[0][accumulator2][1]
            accumulator2 += 1
        print("Minimum Longitude: {0:6f}".format(minlong)) 
        print("Maximum Longitude: {0:6f}".format(maxlong)) 
        print("Minimum Latitude:  {0:6f}".format(minlat))  
        print("Maximum Latitude:  {0:6f}".format(maxlat))
        print("")
        accumulator += 1 
geojsondict("C:/VSProjects/states.json")

