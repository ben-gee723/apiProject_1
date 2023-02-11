# api project
# 1. Find an API
# 2. Import the information
# 3. Analyse the information
# 4. Send the information as a text to a phone

# imports
import configparser
from collections import namedtuple, defaultdict
from itertools import product
import feedparser
import requests

City = namedtuple('City', 'name country description currtemp mintemp maxtemp')

# messaging service -> wazo instead of twilio

# 1. Find an API
### Country Api
### WEATHERAPI
#cityName = "Perth"
weatherKey = "6ca342c4c6976ce9ec0a15d8f5d0a690"
WEATHERAPI = f'https://api.openweathermap.org/data/2.5/weather?appid={weatherKey}&'


# sub functions
# 2. fetch API information

def parse_text_generator_params(config):
    """Return dict of lists of Fuelwatch parameters."""
    weather_param_field = ('q')
    weather_params = defaultdict(list)

    parameter = config['WEATHER PARAMS'][weather_param_field]
#	parameter = input('What country?/n')
    if parameter:
    	weather_params[weather_param_field] = parameter.split(",")
    return weather_params


# kwargs --> KeyWord ARGumentS
def format_url(feed_url, **kwargs):
	"""Format URLs for the FuelWatch RSS feed."""
	pairs = (product([key], value) for (key, value) in kwargs.items())
	print(pairs)
	joined_pairs = (map('='.join, pair) for pair in pairs)
	print(joined_pairs)
	urls = [feed_url + '&'.join(args) for args in product(*joined_pairs)]
	print(urls)
	return urls

def kelvin_to_celsius(kelvin):
	return kelvin - 273.15;


# 3. analyse and format data

def parse_feed(url_set):
#	print("url_set", url_set)
	"""Parse the RSS feeds and return list of station summaries."""

	if isinstance(url_set, str):
		# Avoid iterating over string in the following loop.
		url_set = [url_set]
#		print("url_set", url_set)

# City = namedtuple('City', 'name country description currtemp mintemp maxtemp')
	city_summary_list = list()
	for url in url_set:
		rss_feed = requests.get(url).json()
#		print(rss_feed['name'])
#		print(rss_feed['weather'][0]['description'])
#		print(rss_feed['main']['temp'])
#		print(rss_feed['main']['temp_min'])
#		print(rss_feed['main']['temp_max'])
#		print(rss_feed['sys']['country'])
		
		city = City(
            name=rss_feed['name'],
            country=rss_feed['sys']['country'],
            description=rss_feed['weather'][0]['description'],
            currtemp=float(kelvin_to_celsius(rss_feed['main']['temp'])),
            mintemp=float(kelvin_to_celsius(rss_feed['main']['temp_min'])),
            maxtemp=float(kelvin_to_celsius(rss_feed['main']['temp_max']))
            )
		city_summary_list.append(city)
	return city_summary_list


# 4.0 send info to someone via text
# 4.1 Format text

# 4.2 Send Text

# main function
def main():
	"""Script entry point."""
	config = configparser.ConfigParser()
	config.read('configfile.ini')

	text_generator_params = parse_text_generator_params(config)
	print(text_generator_params)
	urls = format_url(WEATHERAPI, **text_generator_params)

	cities = parse_feed(urls)
	print(cities)


# run main
if __name__ == "__main__":
	main() 