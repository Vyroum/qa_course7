import os.path
import time
import pytest
from selene import browser, query
from selenium import webdriver
import requests
from script_os import TMP_DIR

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": TMP_DIR,
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

browser.config.driver = driver
browser.open("https://gitlab.cc-asp.fraunhofer.de/ise621/sample-python-project/-/blob/develop/README.md")
download_link = browser.element("[data-testid='download-button']").get(query.attribute("href"))
print(download_link)
content = requests.get(url=download_link).content
with open(os.path.join(TMP_DIR, "README2.md"), 'wb') as file:
    file.write(content)

def test_download():
    with open(os.path.join(TMP_DIR, "README2.md")) as file:
        file_content = file.read()
        assert "sphinx-apidoc" in file_content
