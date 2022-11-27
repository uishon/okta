#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys


def cookie():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(os.environ.get("VPN_HOST", sys.argv[:-1]))
    cookie = WebDriverWait(driver, timeout=120).until(lambda d: d.get_cookie('SVPNCOOKIE'))['value']
    driver.quit()
    print(cookie)


if __name__ == "__main__":
    cookie()