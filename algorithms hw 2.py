def geojsonstr(jsonfile):
    filein = open(jsonfile,'r')
    stringin = filein.read()
    #close the file
    filein.close()

    rest_list = []
    start = 0 
    while stringin.find("coordinates",start) != -1:
        inner_list = []
        start = stringin.find("coordinates",start) + 14
        end = stringin.find(",",start)
        # print(stringin[start:end])
        inner_list.append(stringin[start:end])
        start = end + 1
        end = stringin.find("]",start)
        # print(stringin[start:end])
        inner_list.append(stringin[start:end])
        start = end + 1
        #coordinates = stringin[162:202]
        #print(coordinates)
        
        # print(stringin.find("USER_Restaurant",start))
        # rest_name = stringin[]
        start = stringin.find("USER_Restaurant",start) + 18
        end = stringin.find(",",start)
        # print(stringin.find("USER_Restraurant") + 19)
        # print(stringin[start:end-1])
        inner_list.append(stringin[start:end-1])
        
        start = stringin.find("USER_Address",start)
        end = stringin.find("}",start)
        # print(stringin[start+15:end-1])
        inner_list.append(stringin[start+15:end-1])
        start = end + 1 
        
        rest_list.append(inner_list)
        
    sorted(rest_list, key=lambda x: x[1])
    print(rest_list)

# print(geojsonstr("MCTYRests.geojson"))

def main(jsonfile):
    return geojsonstr(jsonfile)
   
main("MCTYRests.geojson")