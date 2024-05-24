from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

username = "username"
password = "password"

def login(driver, username, password):
    try:
        driver.get("https://www.instagram.com/")

        wait = WebDriverWait(driver, 10)

        user_name_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        user_name_field.send_keys(username)

        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(password)

        sign_in_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        sign_in_button.click()

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Home"]')))
    except Exception as e:
        print(f"An error occurred during login: {e}")
        driver.quit()

def open_the_post_view_comment(driver, post_url):
    try:
        driver.get(post_url)
        print("Post loaded successfully.")
        time.sleep(5) 

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        class_names = ["x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]

        for class_name in class_names:
            elements = soup.find_all(class_=class_name)
            for element in elements:
                comment = element.text.strip()
                print(comment)

    except Exception as e:
        print(f"An error occurred while fetching the post: {e}")

options = ChromeOptions()
options.add_argument("--start-maximized")
driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
login(driver, username, password)

post_url = "https://www.instagram.com/p/C7WG-dqyDDjJFLttf0K8wDXTj6Gk710GFVVwQk0/"

open_the_post_view_comment(driver, post_url)

driver.quit()
















# from selenium.webdriver import Chrome, ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# username = "grower_6_"
# password = "Legendfamily14"

# def login(driver, username, password):
#     try:
#         driver.get("https://www.instagram.com/")

#         wait = WebDriverWait(driver, 10)

#         user_name_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
#         user_name_field.send_keys(username)

#         password_field = driver.find_element(By.NAME, 'password')
#         password_field.send_keys(password)

#         sign_in_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
#         sign_in_button.click()

#         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Home"]')))
#     except Exception as e:
#         print(f"An error occurred during login: {e}")
#         driver.quit()

# def open_the_post_view_comment(driver, post_url):
#     try:
#         driver.get(post_url)
#         print("Post loaded successfully.")
#         time.sleep(60) 
#     except Exception as e:
#         print(f"An error occurred while fetching the post: {e}")


# options = ChromeOptions()
# options.add_argument("--start-maximized")
# driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
# login(driver, username, password)

# post_url = "https://www.instagram.com/p/C7WG-dqyDDjJFLttf0K8wDXTj6Gk710GFVVwQk0/"

# open_the_post_view_comment(driver, post_url)

# driver.quit()





















# from selenium.webdriver import Chrome, ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# username = "grower_6_"
# password = "Legendfamily14"

# def login(username, password):
#     try:
#         options = ChromeOptions()
#         options.add_argument("--start-maximized")

#         driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         driver.get("https://www.instagram.com/")

#         wait = WebDriverWait(driver, 10)

#         user_name_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
#         user_name_field.send_keys(username)  # Use the variable username here

#         password_field = driver.find_element(By.NAME, 'password')
#         password_field.send_keys(password)  # Use the variable password here

#         sign_in_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
#         sign_in_button.click()

#         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Home"]')))

#         time.sleep(60)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         driver.quit()

# # login(username, password)
# # print(username, password)

# def fetch_profile_post():
#     try:
#         options = ChromeOptions()
#         options.add_argument("--start-maximized")
#         driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         driver.get("https://www.instagram.com/grower_6_/")
#         profile_post = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Ae"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[2]/div/div/div[2]/a') 

#     except Exception as e:
#         print(f"An error occurred: {e}")