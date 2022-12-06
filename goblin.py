import browser_cookie3
import webbrowser
import requests
import os

day = input()
url = "https://adventofcode.com/2022/day/" + day
url_input = "https://adventofcode.com/2022/day/" + day

if not os.path.exists(day + "_SexyCurryboy"):
    os.mkdir("C:/Users/Sven/Documents/GitHub/advent-of-code-2022/" + day + "_SexyCurryboy")

webbrowser.open(url, new=2)

cj = browser_cookie3.firefox()
if not (".adventofcode.com" in str(cj)):
    cj = browser_cookie3.chrome()

webpage = requests.get(f"https://adventofcode.com/2022/day/" + day + "/input", cookies = cj)
input = open("C:/Users/Sven/Documents/GitHub/advent-of-code-2022/" + day + "_SexyCurryboy/input.txt", "w")
input.write(webpage.text)
input.close()

f = open("C:/Users/Sven/Documents/GitHub/advent-of-code-2022/" + day + "_SexyCurryboy/day" + day + ".py", "w")