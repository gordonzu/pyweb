###############################
# functional_tests.py
# Gordon Zuehlke 3-11-20
###############################

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title


