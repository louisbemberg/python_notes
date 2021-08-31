import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
  address = input('Enter Location: ')
  if len(address) < 1: break

  # makes the text appear like a proper URL with %?& etc.
  url = serviceurl + urllib.parse.urlencode(
    {'address': address})

  print('Retrieving', url, '...')

  uh = urllib.request.urlopen(url)
  data = uh.read().decode()

  print('Retrieved', len(data), 'characters')

  try:
    js = json.loads(data)
  except:
    js = None

  if not js or 'status' not in  js or js['status'] != 'OK':
    print('=== Failure to Retrieve===')
    print(data)
    continue

  print(json.dumps(js, indent=4))

  lat = js["results"][0]["geometry"]["location"]["lat"]
  lng = js["results"][0]["geometry"]["location"]["lng"]
  location = js["results"][0]['formatted_address']

  print('lat:', lat)
  print('lng:', lng)
  print('location:', location)
