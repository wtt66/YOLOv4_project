from selenium import webdriver
import time
from urllib import request


chrome=webdriver.Chrome()
chrome.maximize_window()
chrome.get('https://image.baidu.com/')
chrome.find_element_by_id('kw').send_keys("戴口罩 真人")
chrome.find_element_by_class_name('s_newBtn').click()

current_window_handle=chrome.current_window_handle
for handle in chrome.window_handles:
    if handle != current_window_handle:
       chrome.switch_to.window(handle)
time.sleep(3)

# for i in range(1,0):
#     chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(0.5)

srcList = chrome.find_elements_by_css_selector('.imgbox')

for i,imgbox in enumerate(srcList):  
    if(i<35):
        continue
    imgbox.click()
    windowsHandles = chrome.window_handles
    chrome.switch_to_window(windowsHandles[len(windowsHandles)-1])    
    
    imgSrcBase64 = chrome.find_element_by_id("currentImg").get_attribute('src')
    request.urlretrieve(imgSrcBase64, "./img/mask" + "{:04d}".format(i) + ".jpg") #下载图片
    
    chrome.close()
    windowsHandles = chrome.window_handles
    chrome.switch_to_window(windowsHandles[len(windowsHandles)-1])    
    chrome.implicitly_wait(30)
    time.sleep(2)
    
    

