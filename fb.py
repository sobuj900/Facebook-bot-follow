from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# ফেসবুক লগইন করার জন্য ফাংশন
def login_to_facebook(driver, phone_number, password):
    driver.get("https://www.facebook.com")
    time.sleep(3)

    phone_input = driver.find_element("id", "email")
    password_input = driver.find_element("id", "pass")

    phone_input.send_keys(phone_number)
    password_input.send_keys(password)

    login_button = driver.find_element("name", "login")
    login_button.click()
    time.sleep(5)

# পেজ তৈরি করার জন্য ফাংশন
def create_facebook_page(driver, page_name, category, profile_photo, cover_photo):
    driver.get("https://www.facebook.com/pages/creation")
    time.sleep(5)

    # পেজ নাম ইনপুট
    page_name_input = driver.find_element("name", "page_name")
    page_name_input.clear()
    page_name_input.send_keys(page_name)

    # ক্যাটাগরি ইনপুট
    category_input = driver.find_element("name", "category")
    category_input.send_keys(category)
    category_input.send_keys(Keys.RETURN)
    
    # প্রোফাইল ফটো আপলোড
    profile_photo_input = driver.find_element("name", "profile_pic")
    profile_photo_input.send_keys(profile_photo)

    # কভার ফটো আপলোড
    cover_photo_input = driver.find_element("name", "cover_photo")
    cover_photo_input.send_keys(cover_photo)

    # পেজ তৈরি করার জন্য "Next" বা "Done" এ ক্লিক করা
    next_button = driver.find_element("xpath", "//*[text()='Next']")  # অথবা Done
    next_button.click()
    time.sleep(5)

# অ্যাড ফ্রেন্ড বা ফলো করার জন্য ফাংশন
def add_friend_or_follow(driver, profile_link):
    driver.get(profile_link)
    time.sleep(5)

    try:
        add_friend_button = driver.find_element("xpath", "//button[contains(text(), 'Add Friend')]")
        add_friend_button.click()
    except:
        try:
            follow_button = driver.find_element("xpath", "//button[contains(text(), 'Follow')]")
            follow_button.click()
        except:
            print("Add Friend or Follow button not found.")
    
    time.sleep(3)

# মূল প্রোগ্রাম
if __name__ == "__main__":
    # আপনার লগইন তথ্য (ম্যানুয়ালি ইনপুট নিতে পারেন)
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")

    # ChromeDriver এর path
    driver = webdriver.Chrome()

    # Facebook এ লগইন
    login_to_facebook(driver, phone_number, password)

    # পেজ তৈরি করার তথ্য
    page_name = input("Enter page name: ")
    profile_photo = input("Enter the path of profile photo: ")
    cover_photo = input("Enter the path of cover photo: ")

    # পেজ তৈরি
    create_facebook_page(driver, page_name, "Business", profile_photo, cover_photo)

    # লিঙ্ক ইনপুট নিয়ে অ্যাড ফ্রেন্ড বা ফলো কাজ সম্পন্ন
    while True:
        profile_link = input("Enter profile link (or 'exit' to stop): ")
        if profile_link.lower() == 'exit':
            break
        add_friend_or_follow(driver, profile_link)

    # ব্রাউজার বন্ধ করা
    driver.quit()
