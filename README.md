# Steam-Game-Price-Checker
A python program which using the steam web API allows you to check the price of a number of games quickly and conveniently from the comfort of your desktop.

# How to set it up
To get this program running on your computer you need to:
1. Download python 3.x (python 3 or above) (www.python.org) 
2. Install dependies - go onto command prompt and type 'pip install requests'
3. Download the python file, as well as the APPid.txt file.
4. Put these files inside any folder, just as long as they are in the same directory
5. Inside the python file, change automaticCurrency to false, if you don't want the steamapi to choose it for you (also use this if you are using a VPN or TOR.) If you do indeed change automaticCurrency to false, then make sure to change DesiredCurrency to the currency that you would like
6.Now that you have the code modified now you can open the file called 'APPid.txt'
7. This file is where you would want to put the game app id in (one line per id please)
8. To get the appid of a game, first browse to the games steam page. Next look at the url of the page (it should look something like this: http://store.steampowered.com/app/220200/Kerbal_Space_Program/)
9. Now looking at the url look for the number between 'app/' and '/<name of the app/game>.' In this case you can see that the app id of Kebal Space Program is 220200. 
10. Take you app id and put it into the APPid file (like I said one line per id please)
11. Finally you can run the python file and it should work!
