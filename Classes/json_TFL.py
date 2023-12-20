import urllib.request, json


class Connection:

    # To call the API and receive data for a particular station and line, one needs to pass the arguments
    # of the station's ID and the line's ID into the init method of an object of the Connection class.

    # As we would like to display trains even after they depart the station, we also need ID's for other stations,
    # to know where the trains are with regards to them leaving our desired station (Holborn).


    # Dictionary for coders (copy and paste the station and line IDs where required):

    # Tube Stations:

    # Holborn Underground Station ID = '940GZZLUHBN'
    # Chancery Lane Underground Station ID (Central Eastbound Leaving Holborn) = '940GZZLUCHL'
    # Tottenham Court Road Underground Station ID (Central Westbound Leaving Holborn) = 'HUBTCR'
    # Covent Garden Underground Station ID (Northern Southbound Leaving Holborn) = '940GZZLUCGN'
    # Russell Square Underground Station ID (Northern Northbound Leaving Holborn) = '940GZZLURSQ'

    
    # Bus Stops:
    # (If you're confused, blame it on TFL, they literally name two stops differently,
    # even if they are across the road and service the same line. Sorry.)

    # 55, 243, 19 and 38 (East - West)

    # Gray's Inn Road Bus Stop ID (Buses going East-West on lines 55, 243, 19 and 38) = '490007391E'
    # Lines travelling West Stop on Platform CP

    # Red Lion Street Bus Stop ID (Lines travelling West leaving Gray's Inn Road (Platform A)) = '490007834F'

    # Lines travelling East Stop on Platform CA (of Gray's Inn Road)

    # Rosebury Avenue Bus Stop ID (Lines travelling East leaving Gray's Inn Road (Platform CU - Lines 55 & 243; Platform CE - 19 & 38)) = '490011679W'



    # 17 and 46 (North - South)

    # Clerkenwell Road / Rosebery Avenue Bus Stop ID (Buses going South on lines 17 and 46 (Platform CD)) = '490015447S'
    # High Holborn / Chancery Lane Station Bus Stop ID (Lines travelling South leaving Clerkenwell Road / Rosebery Avenue (Platform C)) = '490008165C'


    # Gray's Inn Road Bus Stop ID (Buses going North on lines 17 and 46 (Platform B)) = '490007391E'
    # Coley Street Bus Stop ID (Lines travelling North leaving Gray's Inn Road (Platform HD)) = '490007598S'


    # Tube lines:
    # Central Line ID = 'central'
    # Piccadilly Line ID = 'piccadilly'

    # Bus lines:
    
    # East-West = Gray's Inn Road

    # North = Gray's Inn Road
    # South = Clerkenwell Road / Rosebery Avenue

    # East-West street stop line 1 = '55'
    # East-West street stop line 2 = '243'
    # East-West street stop line 3 = '19'
    # East-West street stop line 4 = '38'
    # North-South street stop line 1  = '17'
    # North-South street stop line 2 = '46'






    def __init__(self, stationID, lineID):
        self.stationIDs = stationID
        self.lineIDs = lineID
        self.APIkey = 'ff733b67fe7247e08f30d356c54f808f'
        self.url = f"https://api.tfl.gov.uk/Line/{self.lineIDs}/Arrivals/{self.stationIDs}?direction=all"
        self.hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'ApiKey': self.APIkey
        }


    def call(self):

        req = urllib.request.Request(self.url, headers=self.hdr)

        req.get_method = lambda: 'GET'
        with urllib.request.urlopen(req) as response:
                
            response_content = response.read()  # Read the response content
            response_string = response_content.decode('utf-8')  # Decode the content

            data = json.loads(response_string)

            for entry in data:
                vehicle_id = entry.get('vehicleId')
                current_location = entry.get('currentLocation')
                line_name = entry.get('lineName')
                direction = entry.get('direction')
                platform_name = entry.get('platformName')
                time_to_station = entry.get('timeToStation')
                towards = entry.get('towards')


                print(f"Vehicle ID: {vehicle_id}, Line: {line_name}, Direction: {direction}, Platform: {platform_name}, Current Location: {current_location}, Time to Station: {time_to_station} seconds, Towards: {towards}")
                return time_to_station

    

conn = Connection('490008165C','47')

conn.call()




