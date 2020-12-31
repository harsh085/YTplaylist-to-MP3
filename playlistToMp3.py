from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import pyautogui as p,time




def ex(k):
    roll=w.find_element_by_id("input")    
    roll.clear()
    roll.send_keys(k)
    time.sleep(1)
    w.find_element_by_id("submit").click()
    # w.find_element_by_class_name("btn btn-dark").click()
    # gi = w.find_elements_by_xpath("//div[@id='buttons']/a[@href]")#.get_attribute('href')
    # gi = w.find_element_by_link_text('Download')
    # print(gi,"harsh")
    # w.find_element_by_name("url").send_keys(Keys.ENTER)
    # w.execute_script('createYouTubeEmbed();')
    # button.click()
    time.sleep(2)
    gi = w.find_elements_by_css_selector("div#buttons>a")#.get_attribute('href')
    for my_href in gi:
        w.get(my_href.get_attribute("href"))
        break
    # roll.send_keys(Keys.ENTER)
    # time.sleep(2)
    # w.close()
    # print(gi)
    time.sleep(2)
    w.get("https://ytmp3.cc/")
    # w.get("https://msvm.000webhostapp.com")
           
        
w = webdriver.Chrome(executable_path='chromedriver.exe')
#w.maximize_window()
plink=p.prompt("Enter playlist link: ")
w.get(plink)
h = []
elems = w.find_elements_by_xpath("//a[@id='thumbnail' and @href]")   #for taking youtube video urls from playlist
for elem in elems:
    h.append(elem.get_attribute("href"))
    
# print(h)
# file2 = open("MyFile1.txt","w")  

w.get("https://ytmp3.cc/")

"""
roll=w.find_element_by_id("youtube-url")    
roll.clear()
roll.send_keys(h[0])
time.sleep(10)
"""

for i in range(1,len(h)):
    try:
        ex(h[i])
    except:
        continue

print("SUccesfully DOwnloaded...")
w.close()
