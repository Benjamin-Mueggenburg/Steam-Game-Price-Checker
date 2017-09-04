#Steam Game Price checker
#By Benjamin
#22/06/17

#Import request, a library which allows python to access WebAPI's in the form of JSON
import requests

#Import os, allows for program to pause at end
import os
#Version number variable (later to be printed)
version = "2.0"
#Author name variable (also later to be printed)
author = "Benjamin Mueggenburg"
#Number which with each game will increase by one, saying "Game 1", "Game 2", etc.
number = 1

#Prints the starting dialogue with the name of the program, the author, version. (\n means new line)
print("STEAM GAME CHECKER\nversion: {}\nAuthor: {}\n================================\n================================".format(version, author))


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
	return [Gamename, intial_price, final_price, discountpercent, currency]

#The PrintInfo function, once inputed with the game's url, appid and number(this was the variable at the top that equals 1) (Next line)
#It will print out all the details about the game in a more unifrom way
def PrintInfo(url,appid,number):
	#Calls the above fuction call GetInformation (meaning that the variable, 'a' is now a list)
	a = GetInformation(url, appid)
	#Prints at the start "Game" and then the game number in the list which is inputed through the variable 'number'
	print("Game {}".format(number))
	#Prints the name of the game, which is stored in 'a' at number 0 in the list
	print("Name: {}".format(a[0]))
	#Prints the intial price and the currency of the game, which is stored in 'a' at number 1 and 4 in the list. It also adds in the $ symbol
	print("Intial Price: ${} {}".format(a[1],a[4]))
	#Prints the final price and the currency of the game, which is stored in 'a' at number 2 and 4 in the list. It also adds in the $ symbol
	print("Final Price: ${} {}".format(a[2],a[4]))
	#Prints the discount perecnt of the game, which is stored in 'a' at number 3 in the list. It also adds in the % symbol for the percent.
	print("Discount Percent: {}%".format(a[3]))

	#a[3] is the discount perecent, so this checks if the discount percent equals zero, meaning there is no deal or special
	if a[3] == 0:
		#Prints a seperation
		print("*******************")
		#If the statement is true, then print out "NO DISCOUNT AT THE MOMENT"
		print("NO DISCOUNT AT CURRENT MOMENT")

	#If the 'if' statement is false, meaning there is a deal, then run the following lines of code
	else:
		#Prints the price reduction, and since there is no variable, it takes the intial price(a[1]) and subtracts the final price(a[2]). It also adds in the currency(a[4])
		print("Price Reduction: ${} {}".format(a[1] - a[2], a[4]))
		#prints out a line of asterisks seperating the line after from all the numbers printed above
		print("*******************")
		#prints out the line "CURRENT DISCOUNT" indicating that there is some sort of deal or special on
		print("CURRENT DISCOUNT")
	#(No matter if the 'if' statement runs or the 'else' this following line will run) this seperates the chosen game from the next
	print("==================================")

#IF YOU WANT TO CHANGE THE GAMES THAT IT DISPLAYS YOU MUST CHANGE THE FOLLOWING STRINGS INSIDE OF THE LIST BELOW
#First find the url of the game you want e.g Kerbal Space program - "http://store.steampowered.com/app/220200/Kerbal_Space_Program/".
#Between /app/ and the name of the game there is a number e.g in kerbal space it's "220200"
#With this number, add a ',' to the end of the last number, then paste your number there. Make sure to add "" marks around the number or it WILL NOT WORK 
Filename = "AppID"
with open('{}.txt'.format(Filename)) as f:
		file = f.read().splitlines()

appId = file[1:]

#["237110", "220200", "274190", "314160","578330","391540"]
#Change for currency (The New Zealand dollar is nzd)
desiredcurrency = "nzd"



#This loop runs for how many strings are in the list called appId
for ID in appId:
	#Creates a temporary url for the game, by inserting the appid into the url below
	tempUrl = "http://store.steampowered.com/api/appdetails/?appids={}&cc={}".format(ID,desiredcurrency)
	#Calls the PrintInfo function on the tempUrl, appid and the local game number (1,2,3 etc.)
	PrintInfo(tempUrl,ID,number)
	#Add's one to number e.g 1 becomes 2, 3 become 4 etc.
	number += 1

os.system("pause")



	
	

