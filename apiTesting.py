import feedparser
import requests
from urllib.parse import urlencode


def check_api(url, key = '',  headers = ""):
	#	test = feedparser.parse()
	response = requests.get(url)
	if headers:
		test = feedparser.parse(url + "?" + urlencode(headers))
	print(response.json())
	return response.json()


### NOT IN USE - WEATHER API
# https://catalogue.data.wa.gov.au/dataset/dpird-apis
WAWEATHERAPI = "https://www.agric.wa.gov.au/weather-api-20"
result = feedparser.parse(WAWEATHERAPI)
# print(result.bozo_exception)
# dict_keys(['feed', 'entries', 'bozo', 'headers', 'etag', 'updated', 'updated_parsed', 'href', 'status', 'encoding', 'bozo_exception', 'version', 'namespaces'])
# check_api(WAWEATHERAPI)



### NOT IN USE - TEXT GENERATION API
# text generation api
# curl \
# Example directly sending a text string:
#	-F 'text=YOUR_TEXT_HERE' \
#	-H 'api-key:quickstart-QUdJIGlzIGNvbWluZy4uLi4K' \
# url = "https://api.deepai.org/api/text-generator/"

# apiKey & auth
HEADERS = {'api-key':'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
TEXTGENERATIONAPI = "https://api.deepai.org/api/text-generator/?"+urlencode(HEADERS)
# print("https://api.deepai.org/api/text-generator/?"+urlencode(HEADERS))
#print(feedparser.parse(TEXTGENERATIONAPI))
# dict_keys(['feed', 'entries', 'bozo', 'headers', 'href', 'status', 'encoding', 'bozo_exception', 'version', 'namespaces'])

# URL from Inspect --> Network
inpectUrl = "https://api.deepai.org/site_search_row_listing/art?query=apple"
# dict_keys(['feed', 'entries', 'bozo', 'headers', 'href', 'status', 'encoding', 'bozo_exception', 'version', 'namespaces'])
#print(check_api(inpectUrl))



### NOT IN USE - TEST - Rick and morty
rickNmortyApi = "https://rickandmortyapi.com/api/character"
#check_api(rickNmortyApi)



### NOT IN USE - Country Facts
countryApi = "https://restcountries.com/v3.1/name/$"



##### WEATHER API --> USING
q = "Perth"
weatherKey = "6ca342c4c6976ce9ec0a15d8f5d0a690"
weatherApi = f'https://api.openweathermap.org/data/2.5/weather?appid={weatherKey}&q={q}'
check_api(weatherApi)
