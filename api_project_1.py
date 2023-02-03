# api project
# 1. find an API
# 2. import the information
# 3. analyse the information
# 4. send the information as a text to a phone

# imports
import configparser
from collections import defaultdict
from itertools import product
import feedparser
from urllib.parse import urlencode

# messaging service -> wazo instead of twilio


# 1. FAPI from DataWa
# https://catalogue.data.wa.gov.au/dataset/dpird-apis
WAWEATHERAPI = "https://www.agric.wa.gov.au/weather-api-20"

# OR
# text generation api
# curl \
# Example directly sending a text string:
#	-F 'text=YOUR_TEXT_HERE' \
#	-H 'api-key:quickstart-QUdJIGlzIGNvbWluZy4uLi4K' \


# apiKey & auth
HEADERS = {'api_key':'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
TEXTGENERATIONAPI = "https://api.deepai.org/api/text-generator/?"+urlencode(HEADERS)
print(urlencode(HEADERS))
test = feedparser.parse(TEXTGENERATIONAPI+'&text=APPLE')
print(test)

# sub functions
# 2. fetch API information

def parse_text_generator_params(config):
    """Return dict of lists of Fuelwatch parameters."""
    text_generator_param_field = ('text')
    text_generator_param = defaultdict(list)

    parameter = "_".join(config['TEXT GENERATOR PARAMS'][text_generator_param_field].split(' '))
#    print(parameter)
    if parameter:
    	text_generator_param[text_generator_param_field] = parameter.split(',')
#    	print(text_generator_param)
#    	text_generator_param[text_generator_param_field] = parameter
    return text_generator_param


# kwargs --> KeyWord ARGumentS
def format_url(feed_url, **kwargs):
	"""Format URLs for the FuelWatch RSS feed."""
	pairs = (product([key], value) for (key, value) in kwargs.items())
#	print(pairs)
	joined_pairs = (map('='.join, pair) for pair in pairs)
#	print(joined_pairs)
	urls = [feed_url + '&'.join(args) for args in product(*joined_pairs)]
#	print(urls)
	return urls


def parse_feed(url_set):
#	print("url_set", url_set)
	"""Parse the RSS feeds and return list of station summaries."""
	if isinstance(url_set, str):
		# Avoid iterating over string in the following loop.
		url_set = [url_set]
#		print("url_set", url_set)

#	for url in url_set:

#		print(feedparser.parse(url, request_headers=HEADERS))
#    station_summary_list = list()
#    for url in url_set:
#        rss_feed = feedparser.parse(url)
#        for entry in rss_feed.entries:
#            station = Station(
#                name=entry.get('trading-name'),
#                address=entry.address,
#                price=float(entry.price),
#                discount=float(fuel_vouchers.get(entry.brand.lower(), 0))
#            )
#            station_summary_list.append(station)
#    return station_summary_list

# 3. analyse and format data

# 4. send info to someone via text

# main function
def main():
	"""Script entry point."""
	config = configparser.ConfigParser()
	config.read('configfile.ini')

	text_generator_params = parse_text_generator_params(config)
#	print(text_generator_params)
	urls = format_url(TEXTGENERATIONAPI, **text_generator_params)

#	stations = parse_feed(urls)
#	print(stations)


# run main
if __name__ == "__main__":
	main() 