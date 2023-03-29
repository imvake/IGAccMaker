from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# import undetected_chromedriver as uc
import string
import itertools
import random
import time
# import undetected_chromedriver as uc
# driver = uc.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('proxy-server=82.117.252.138:13837')

browser = webdriver.Chrome()
browser = webdriver.Chrome('D:/Software/python/chromedriver_win32/chromedriver_win32/chromedriver.exe', options=options)

browser.get("https://www.instagram.com/accounts/emailsignup/")



time.sleep(9)



##### Temp Emails #####
from mailtm import Email

def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])

# Get Domains
test = Email()
print("\nDomain: " + test.domain)

# Make new email address
test.register()
print("\nEmail Adress: " + str(test.address))

# Start listening
test.start(listener)
print("\nWaiting for new emails...")

##### generate Emails #####
emailist = []
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

all_combos = list(itertools.combinations(letters,7)) #make all 7 letter combinations
all_combos = [''.join(combo) for combo in all_combos] #make them strings
email = random.sample(all_combos,1)[0]+'@gmail.com' #grab a random one, add @gmail.com
emailist.append(email)
########################################

##### fullname #####

fullnamelist = []
all_combos = list(itertools.combinations(letters,9)) #make all 7 letter combinations
all_combos = [''.join(combo) for combo in all_combos] #make them strings
fullname = random.sample(all_combos,1)
fullnamelist.append(fullname)
########################################

##### Username #####
usernamelist = []
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

all_combos = list(itertools.combinations(letters,9)) #make all 7 letter combinations
all_combos = [''.join(combo) for combo in all_combos] #make them strings
uname = random.sample(all_combos,1)[0]+"_test"#grab a random one, add @gmail.com
usernamelist.append(uname)
########################################

##### password #####

passwordlist = []
characters = string.ascii_letters + string.punctuation  + string.digits

Pass = ""
password_length = random.randint(8, 16)

for x in range(password_length):
    char = random.choice(characters)
    Pass = Pass + char
passwordlist.append(Pass)


########################################
NameorPhone = WebDriverWait(browser , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='emailOrPhone']")))
NameorPhone.clear()
NameorPhone.send_keys(str(test.address))

fname = WebDriverWait(browser , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='fullName']")))
fname.clear()
fname.send_keys(fullname)

username = WebDriverWait(browser , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
username.clear()
username.send_keys(uname)

password = WebDriverWait(browser , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
password.clear()
password.send_keys(Pass)


time.sleep(2)
register = WebDriverWait(browser , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

bday = WebDriverWait(browser , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[25]"""))).click()

bnext = WebDriverWait(browser , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button"""))).click()


acc_info = {"Email":str(test.address), "Full Name":fullnamelist, "UserName":usernamelist, "Password":passwordlist}


print(acc_info)
print("Email ",str(test.address))
print("Full Name ",fullnamelist)
print("User Name ",usernamelist)
print("Password ",passwordlist)

# time.sleep(1000)
