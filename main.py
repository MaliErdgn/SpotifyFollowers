from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service(r"C:\Users\Mali\Desktop\Codes\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://accounts.spotify.com/tr/login")

mail = driver.find_element(By.ID, "login-username")
mail.send_keys("memokingxd6879")

password = driver.find_element(By.ID, "login-password")
password.send_keys("SpotifyBot")

driver.find_element(By.ID,"login-button").click()

time.sleep(5)

driver.get("https://open.spotify.com/user/ezsmk9j1kdyzkows879ia4hsf/followers") #Mali
# driver.get("https://open.spotify.com/user/11164490697/followers") #Bertan
# driver.get("https://open.spotify.com/user/jurumai/followers") #Bartu
# driver.get("https://open.spotify.com/user/21b256q6yctjxc37736r63uky/followers") #Efe
# driver.get("https://open.spotify.com/user/gamze_erdgn/followers") #Ablam
# driver.get("https://open.spotify.com/user/zeh.dem14/followers") #reyyan 

time.sleep(5)

followersWeb = driver.find_elements(By.CLASS_NAME,"nk6UgB4GUYNoAcPtAQaG") #Find followers' web elements 
followers = []
for follower in followersWeb:  # iterate through the followers' web elements to get the names of the followers 
    followers.append(follower.text) # add them to the followers list


driver.get("https://open.spotify.com/user/ezsmk9j1kdyzkows879ia4hsf/following") #Mali
# driver.get("https://open.spotify.com/user/11164490697/following") #Bertan
# driver.get("https://open.spotify.com/user/jurumai/following") #Bartu
# driver.get("https://open.spotify.com/user/21b256q6yctjxc37736r63uky/following") #Efe
# driver.get("https://open.spotify.com/user/gamze_erdgn/following") #Ablam
# driver.get("https://open.spotify.com/user/zeh.dem14/following") #reyyan

time.sleep(5)

followingWeb = driver.find_elements(By.CLASS_NAME, "nk6UgB4GUYNoAcPtAQaG") # find web elements of following
followings = []
for following in followingWeb: # iterate through the followings web elements to get the names of the followings 
    followings.append(following.text) #add them to the followings list 

notFollowingMeBack = [x for x in followings if x not in followers] #Checking if an element is in followings but not in followers (They are not following me back)
iDontFollowBack = [x for x in followers if x not in followings] #Checking if an element is in followers but not in followings (I am not following them back)

print("Not following me back: " + str(notFollowingMeBack))
print("I dont follow back: " + str(iDontFollowBack))
