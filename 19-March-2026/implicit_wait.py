''' implicitly wait used/works for find_element method only
drawback : it will not care about if the element is interactable or not.
It is a global wait like we only use this once and this will works on whole code
It saves time as it starts interacting as soon as it finds the element in DOM structure as
It will skip the remaining
second if the in parameter it is given like 6 second but the element is found in 1 second it will skip remaining 5 sec
Dont use both wiats together (implicit and explicit wait)
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
