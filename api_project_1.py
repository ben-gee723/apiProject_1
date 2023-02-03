# api project
# 1. find an API
# 2. import the information
# 3. analyse the information
# 4. send the information as a text to a phone

# imports
import configparser

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

# 3. analyse and format data

# 4. send info to someone via text

# main function
def main():
	"""Script entry point."""
	config = configparser.ConfigParser()
	config.read('configfile.ini')
	print()

# run main

if __name__ == "__main__":
	main() 