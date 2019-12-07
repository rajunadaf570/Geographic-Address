#python imports.
import requests

# django imports.
from django.conf import settings

#app level imports.
from .exceptions import NetworkException

URL = settings.LOCATIONIQ_URL

def getlatlon(address, key, url=URL):
	"""
	This function is used to get the latitude and longitude address.
	"""
	PARAMS = {}
	PARAMS['key'] = key
	PARAMS['q'] = address

	try: 
		response = requests.get(url=url, params=PARAMS)
		if response.status_code == 200:
			data = response.json()
			lat = data[0]['lat'] 
			lon = data[0]['lon']
			return lat, lon

	except Exception as e:
		print(str(e))
		raise NetworkException(errors=str(e))
		
	return 0, 0










