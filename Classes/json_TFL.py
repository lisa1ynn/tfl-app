import urllib.request, json

# try:
#     url = "https://api.tfl.gov.uk/Line/central,piccadilly/Arrivals/940GZZLUHBN?direction=all"

#     hdr ={
#     # Request headers
#     'Cache-Control': 'no-cache',
#     }

#     req = urllib.request.Request(url, headers=hdr)

#     req.get_method = lambda: 'GET'
#     response = urllib.request.urlopen(req)
#     print(response.getcode())
#     print(response.read())
# except Exception as e:
#     print(e)


class Connection:

    def __init__(self):
        self.stationIDs = ('940GZZLUHBN')
        self.lineIDs = ('central,piccadilly')
        self.url = f"https://api.tfl.gov.uk/Line/{self.lineIDs}/Arrivals/{self.stationIDs}?direction=all"
        self.hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
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

    

conn = Connection()

conn.call()
