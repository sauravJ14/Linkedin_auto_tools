from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
USER_NAME="YOUR_ID"
PASSWORD="YOUR_PW"
import time

driver_ser=Service(executable_path="D:\py prac\chromedriver.exe")
driver=webdriver.Chrome(service=driver_ser)
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
# ------------------------------------------------------------------------------------------------------------Withdraw--------------------------------------------------------------------------------------------------------
people=21

def reject():
    while people:
        reject_btn = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section/div[2]/ul/li[1]/div/div[2]/button/span")
        reject_btn.click()
        withdraw=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]/span')
        withdraw.click()
        driver.refresh()
def login():
    # choice_of_login=input("enter 1 to enter ID Pass \n enter 2 for login wiith Google")
    # if choice_of_login=="1":
            sign_in=driver.find_element(By.XPATH,'/html/body/div[1]/main/p[1]/a')
            sign_in.click()
            u_name=driver.find_element(By.XPATH,'//*[@id="username"]')
            u_name.send_keys(USER_NAME)
            password=driver.find_element(By.XPATH,'//*[@id="password"]')
            password.send_keys(PASSWORD)
            f_sign_in=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
            f_sign_in.click()

# else :
    #     google=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]')
    #     google.click()


try:
    reject()
except:
  login()
  reject()


