#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 10:19
# @Author  : Yang

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver.implicitly_wait(10) #（2）隐形等待 全局超时时间  设置等待时间 满足条件 立马执行 不用等待到设置的时间
driver.get("file:///C:/Users/Administrator/Desktop/File/Wait.html")
sleep(2)
driver.find_element_by_id("b").click()
# sleep(10) #（1）sleep强制等待  设置的时间 即使条件已经可执行 但是必须等待设置的时间 不提前执行
WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".red_box"))) #（3）显性等待 页面能找到.red_box 就执行
# 20-timeout  0.5-扫屏幕间隔
element = driver.find_element_by_class_name("red_box")
driver.execute_script("arguments[0].style.border = \"5px solid yellow\"", element)
sleep(2)
driver.quit()
