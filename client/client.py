import sys
import requests
import json
from pprint import pprint

base_url = 'http://0.0.0.0:5000'

def send_request():
    url = base_url + '/'
    response = requests.get(url)
    return response

if __name__ == '__main__':
    while(True):
        read = ""
        #try:
        read = input("Input Command: ")
        #except EOFError as e:
        #    print(end="")
        cmd = read.split( )

        if (len(cmd) == 0):
            pass

        elif ((cmd[0] == "showReservation") and (len(cmd) == 2)):

            url = base_url + '/showReservation'
            params = {'reservationId':cmd[1]}
            response = requests.post(url=url, json=params)
            json_data = json.loads(response.text)

            print('> ' + str(json_data))

        elif ((cmd[0] == "reserveMovie") and (len(cmd) == 3)):

            url = base_url + '/reserveMovie'
            params = {'movieId':cmd[1], 'nrOfSeats':cmd[2]}
            response = requests.post(url=url, json=params)

            print('> ' + str(response.json()))

        else:
            print("> Wrong command")
