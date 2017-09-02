import urllib.request, json
import pprint
import re
import requests
import urllib
# import sys

class Googleapi_test():

    def __init__(self):
        '''
        ihihi
        '''
    def decode(self, URL2):
        for i in range(len(URL2)-2):           
            temp = URL2[i]+URL2[i+1]+URL2[i+2] 
            if temp == '%26':                  
                URL2 = URL2[:i]+'&'+URL2[i+3:] 
                #print( URL2)
                #print('\n 1 \n')
                return(self.decode(URL2))

            elif temp == '%2C':                
                URL2 = URL2[:i]+','+URL2[i+3:] 
                return(self.decode(URL2))
        return (URL2)
    def googleapi(self, destination, lat, lon):
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        #lat = str(j['latitude'])
        #lon = str(j['longitude'])
        lat = str(lat)
        lon = str(lon)
        print (lat )
        print (lon )
        print ('\n' )
        destination = destination.decode('big5')
        #print(destination)
        # destination = ''
        # for i in sys.argv[1:]:
        # 	destination = destination + i 
        URL2 = "https://maps.googleapis.com/maps/api/directions/json?mode=walking&language=zh-TW&origin=%s,%s&destination=%s&key=AIzaSyA1IwGCXckmkgbhZ5UVOYaS4eS6nUEkXTs"%(lat,lon,destination)

        #print (0)
        URL2 = urllib.parse.quote(URL2, ':?=/')
        #print(URL2)
        URL2 = self.decode(URL2)
        #print(URL2)
        googleResponse = urllib.request.urlopen(URL2)
        #print(0)
        
        googleResponse = googleResponse.readall().decode('utf-8')
        
        jsonResponse = json.loads(googleResponse)
        #pprint.pprint(jsonResponse)
        if not jsonResponse['routes']:
            return('無此地名')
        
        steps = jsonResponse['routes'][0]['legs'][0]['steps']
        
        total_distance = jsonResponse['routes'][0]['legs'][0]['distance']['text']
        total_time = jsonResponse['routes'][0]['legs'][0]['duration']['text']
        allsteps = '總距離為' +total_distance + '\n' +'總時間為' +total_time +'\n'


        for i in range(len(steps)):
            distance     = steps[i]['distance']['text']
            times        = steps[i]['duration']['text']
            directions = steps[i]['html_instructions']
            #allsteps = allsteps + '距離還有' + distance +'\n'
            #allsteps = allsteps + '時間為' + times +'\n'
            Directions = ''
            no_skip = True
            for a in range(len(directions)): 
                if no_skip: 
                    if directions[a] == '<':
                        no_skip = False
                    else:
                        Directions = Directions + directions[a]
                elif directions[a] == '>':
                    no_skip = True
                    Directions = Directions + ' '	
            allsteps = allsteps + '' + Directions +'\n'
            allsteps = allsteps + '距離還有' + distance +'\n' 
            allsteps = allsteps + '時間為' + times +'\n'
        print (allsteps)
        return (allsteps)




