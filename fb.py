import os
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ম্যানুয়ালি ইনপুট
EMAIL = input("Enter Your Email/Number: ")
PASSWORD = input("Enter Your Password: ")
profile_folder = input("Enter Your Pp Folder Path: ")
cover_folder = input("Enter Your Cp Folder Path: ")
name_file_path = input("Enter Your Page Name File Path (e.g., name.txt): ")
user_link_count = int(input("How many user links will you provide? "))

user_links = []
for i in range(user_link_count):
    user_link = input(f"Enter user link {i + 1}: ")
    user_links.append(user_link)

# ChromeDriver সেটআপ করা (headless mode)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Facebook লগিন পেজে যাও
driver.get("https://www.facebook.com/login")

# ইমেইল বা ফোন নম্বর ইনপুট ফিল্ড
email_box = driver.find_element(By.XPATH, "//input[@name='email']")
email_box.send_keys(EMAIL)

# পাসওয়ার্ড ইনপুট ফিল্ড
password_box = driver.find_element(By.XPATH, "//input[@name='pass']")
password_box.send_keys(PASSWORD)

# লগিন বাটন
login_button = driver.find_element(By.NAME, "login")
login_button.click()

time.sleep(5)

# নামের ফাইল থেকে পেজের নাম পড়া
with open(name_file_path, 'r') as file:
    names = file.readlines()

# লুপের মাধ্যমে পেজ তৈরি করা
while True:
    for index in range(len(names)):
        name = names[index].strip()
        category = "Business" 

        # পেজ তৈরি
        driver.get("https://www.facebook.com/pages/create/")
        page_name = driver.find_element(By.XPATH, "//input[@name='name']")
        page_name.send_keys(name)

        category_box = driver.find_element(By.XPATH, "//input[@name='category']")
        category_box.send_keys(category)

        profile_pictures = [f for f in os.listdir(profile_folder) if f.endswith('.jpg')]
        cover_pictures = [f for f in os.listdir(cover_folder) if f.endswith('.jpg')]
        
        selected_pp = random.choice(profile_pictures)
        selected_cp = random.choice(cover_pictures)

        # প্রোফাইল ছবি
        profile_picture_path = os.path.join(profile_folder, selected_pp)
        profile_picture = driver.find_element(By.XPATH, "//input[@type='file']")
        profile_picture.send_keys(profile_picture_path)

        # কভার ছবি
        cover_picture_path = os.path.join(cover_folder, selected_cp)
        cover_picture = driver.find_element(By.XPATH, "//input[@type='file' and @name='cover_photo']")
        cover_picture.send_keys(cover_picture_path)

        next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next') or contains(text(), 'Done')]")
        next_button.click()

        time.sleep(5)

        driver.get(f"https://www.facebook.com/{name}")

        for link in user_links:
            driver.get(link)
            time.sleep(3)

            try:
                if "Follow" in driver.page_source:
                    follow_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Follow')]")
                    follow_button.click()
                elif "Add Friend" in driver.page_source:
                    add_friend_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Friend')]")
                    add_friend_button.click()
            except Exception as e:
                print(f"Error while processing {link}: {e}")

            time.sleep(5)

# driver.quit() # এই লাইনটি স্ক্রিপ্টের শেষে ব্যবহার করুন
