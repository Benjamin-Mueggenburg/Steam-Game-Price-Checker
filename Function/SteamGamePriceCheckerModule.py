#Steam Game Price checker
#By Benjamin
#6/09/17

#Import request, a library which allows python to access WebAPI's in the form of JSON
import requests

class SteamGameChecker:
	def __init__(self,desiredcurrency,automaticCurrency=True):
		self.desiredcurrency = desiredcurrency
		self.automaticCurrency = autmaticCurrency


#The GetInformation function, once inputed with the url for the steam game in the JSON api format and the app's id (Next line)
#The function will return a list of the game's name, intial price, final price, discount percent and the currency
	def GetInformation(url,appid):
		#Accesses the WEBapi through the url
		respose = requests.get(url)
		#Opens the WEBapi in a json form
		j = respose.json()

		#Gamename is the variable storing the name of the game
		Gamename = j["{}".format(appid)]["data"]["name"]

		#Pre_intial_price is the variable storing the intial price of the product, but the json file doesn't put in decimal places for price (e.g $14.99 become 1499)
		pre_intial_price = j["{}".format(appid)]["data"]["price_overview"]["initial"]
		#intial_price is the pre_intial_price but converted into a float and divided by 100, this variable is used instead of pre_intial_price
		intial_price = float(pre_intial_price) / 100

		#Pre_final_price is the variable storing the final price of the product, but the json file doesn't put in decimal places for price (e.g $14.99 become 1499)
		pre_final_price = j["{}".format(appid)]["data"]["price_overview"]["final"]
		#final_price is the pre_final_price but converted into a float and divided by 100, this variable is used instead of pre_final_price
		final_price = float(pre_final_price) / 100

		#discountpercent is the variable storing the discount percent of the game e.g 10, or 75 (it doesn't include the % symbol)
		discountpercent = j["{}".format(appid)]["data"]["price_overview"]["discount_percent"]
		#currecy is the variable storing the currency of the prices of the game e.g NZD
		currency = j["{}".format(appid)]["data"]["price_overview"]["currency"]
		#returns all the variables in the form of a list
		return {"gamename":Gamename, "intialprice":intial_price, "finalprice":final_price, "discountpercent":discountpercent, "currency":currency}



