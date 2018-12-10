from urllib.request import urlopen
import json
import sys

def getWeather(location):
    APIKEY = ':)'
    URL = f'http://api.apixu.com/v1/current.json?key={APIKEY}&q={location}'

    try:
        with urlopen(URL) as res:
            junk = res.read().decode('utf-8')
            data = json.loads(junk)
            location = data['location']['name']
            country = data['location']['country']
            time = data['location']['localtime']
            temp = data['current']['temp_c']
            dayTime = 'Day' if data['current']['is_day'] == 1 else 'Night'
            weather = data['current']['condition']['text']
    
            print(f'Location: {location} - {country} | Time: {time} - {dayTime} | Temp: {temp} celcius | condition: {weather}.')
    except:
        print("Wrong Parameter or Server is Down! Try again Later.")


if __name__=='__main__':
    if sys.argv[1] is None:
        print('Enter a City Name...')
    elif sys.argv[1] == '-h':
        print('\t\t- Quick Weather -\n\t<usage ->  qw <parameter:City Name>')
    elif sys.argv[1] == '.':
        print('Fetching Weather...')
        getWeather("Eskisehir")
    else:
        print('Fetching Weather...')
        getWeather(sys.argv[1])
