import feedparser
import requests
from urllib.parse import urlencode


def check_api(url, headers = ""):
	#	test = feedparser.parse()
	response = requests.get(url)
	if headers:
		test = feedparser.parse(url + "?" + urlencode(headers))
	print(response.json())
#	return test.keys()


##### WEATHER API
# https://catalogue.data.wa.gov.au/dataset/dpird-apis
WAWEATHERAPI = "https://www.agric.wa.gov.au/weather-api-20"
result = feedparser.parse(WAWEATHERAPI)
# print(result.bozo_exception)
# dict_keys(['feed', 'entries', 'bozo', 'headers', 'etag', 'updated', 'updated_parsed', 'href', 'status', 'encoding', 'bozo_exception', 'version', 'namespaces'])
# check_api(WAWEATHERAPI)



##### TEXT GENERATION API
# text generation api
# curl \
# Example directly sending a text string:
#	-F 'text=YOUR_TEXT_HERE' \
#	-H 'api-key:quickstart-QUdJIGlzIGNvbWluZy4uLi4K' \
# url = "https://api.deepai.org/api/text-generator/"

# apiKey & auth
HEADERS = {'api_key':'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
TEXTGENERATIONAPI = "https://api.deepai.org/api/text-generator/?"+urlencode(HEADERS)
# dict_keys(['feed', 'entries', 'bozo', 'headers', 'href', 'status', 'encoding', 'bozo_exception', 'version', 'namespaces'])

# URL from Inspect --> Network
inpectUrl = "https://api.deepai.org/site_search_row_listing/art?query=apple"
# dict_keys(['feed', 'entries', 'bozo', 'headers', 'href', 'status', 'encoding', 'bozo_exception', 'version', 'namespaces'])
print(check_api(inpectUrl))



### TEST - Rick and morty
rickNmortyApi = "https://rickandmortyapi.com/api/character"
# check_api(rickNmortyApi)