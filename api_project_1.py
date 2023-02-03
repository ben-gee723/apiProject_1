# api project
# 1. find an API
# 2. import the information
# 3. analyse the information
# 4. send the information as a text to a phone

# imports
import configparser
from collections import defaultdict

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
TEXTGENERATIONAPI = "https://api.deepai.org/api/text-generator" 

# sub functions
# 2. fetch API information

def parse_text_generator_params(config):
    """Return dict of lists of Fuelwatch parameters."""
    text_generator_param_field = ('text')
    text_generator_param = defaultdict(list)
    print(text_generator_param)

    parameter = config['TEXT GENERATOR PARAMS'][text_generator_param_field]
    if parameter:
    	text_generator_param[text_generator_param_field] = parameter.split(',')
    
    return text_generator_param

# 3. analyse and format data

# 4. send info to someone via text

# main function
def main():
	"""Script entry point."""
	config = configparser.ConfigParser()
	config.read('configfile.ini')

	text_generator_params = parse_text_generator_params(config)
	print()

# run main

if __name__ == "__main__":
	main() 