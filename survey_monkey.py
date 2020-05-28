import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")
driver = webdriver.Chrome(executable_path=r"M:\python\Lib\site-packages\chromedriver.exe", chrome_options=chrome_options)
driver.get('https://www.surveymonkey.co.uk/r/8QTQS6P')

#first ok button
time.sleep(1)
ok_btn = driver.find_element_by_xpath("//button[@type='submit' and contains(., 'OK')]")
driver.execute_script("arguments[0].click();", ok_btn)
time.sleep(1)

#first question
#female option
#q1_btn = driver.find_element_by_xpath("//label[@for='135735679_973000306']")
#q1_btn.click()

#male option
q1_btn = driver.find_element_by_xpath("//label[@for='135735679_973000307']")
q1_btn.click()

#other option
#q1_btn = driver.find_element_by_xpath("//label[@for='135735679_973000308']")
#q1_btn.click()
time.sleep(1)


#second question
#20-30
#q2_btn = driver.find_element_by_xpath("//label[@for='135735852_973001608']")
#q2_btn.click()

#31-40
#q2_btn = driver.find_element_by_xpath("//label[@for='135735852_973001609']")
#q2_btn.click()

#41-50
q2_btn = driver.find_element_by_xpath("//label[@for='135735852_973001610']")
q2_btn.click()

#over 51
#q2_btn = driver.find_element_by_xpath("//label[@for='135735852_973001611']")
#q2_btn.click()
time.sleep(1)

#3rd question
#East/South East Asian
q3_btn = driver.find_element_by_xpath("//label[@for='135736052_973002698']")
q3_btn.click()

#Middle/South Asian
#q3_btn = driver.find_element_by_xpath("//label[@for='135736052_973002699']")
#q3_btn.click()

#European
#q3_btn = driver.find_element_by_xpath("//label[@for='135736052_973002700']")
#q3_btn.click()

#African
#q3_btn = driver.find_element_by_xpath("//label[@for='135736052_973002701']")
#q3_btn.click()

#American/Latin American
#q3_btn = driver.find_element_by_xpath("//label[@for='135736052_973002702']")
#q3_btn.click()

#Australia
#q3_btn = driver.find_element_by_xpath("//label[@for='135736052_973002703']")
#q3_btn.click()

#Prefer not to say
#q3_btn = driver.find_element_by_xpath("//label[@for='135736052_973002704']")
#q3_btn.click()
time.sleep(1)

#4th question
#Yes, I am living in Tokyo
q4_btn = driver.find_element_by_xpath("//label[@for='135736335_973004000']")
q4_btn.click()

#Yes, I have been there and want to come back
#q4_btn = driver.find_element_by_xpath("//label[@for='135736335_973004001']")
#q4_btn.click()

#Yes, I have been there but do not want to come back
#q4_btn = driver.find_element_by_xpath("//label[@for='135736335_973004002']")
#q4_btn.click()

#Not yet, I intended to visit in future
#q4_btn = driver.find_element_by_xpath("//label[@for='135736335_973004003']")
#q4_btn.click()

#No, and I do not have intention to visit
#q4_btn = driver.find_element_by_xpath("//label[@for='135736335_973004004']")
#q4_btn.click()

time.sleep(1)

#question 5
q5_btn = driver.find_element_by_name('135736673')
q5_btn.send_keys("cool, cooler, coolest")

ok_btn = driver.find_element_by_id('135736673-ok')
driver.execute_script("arguments[0].click();", ok_btn)
time.sleep(1)

#question 6
#Yes
q6_btn = driver.find_element_by_xpath("//label[@for='135737423_973011447']")
q6_btn.click()

#No
#q4_btn = driver.find_element_by_xpath("//label[@for='135737423_973011448']")
#q4_btn.click()

time.sleep(1)

#question 7
#Yes
q7_btn = driver.find_element_by_xpath("//label[@for='135737509_973011919']")
q7_btn.click()

#No
#q7_btn = driver.find_element_by_xpath("//label[@for='135737509_973011920']")
#q7_btn.click()

time.sleep(1)

#question 8
#Story plot, message, inpsiration
q8_btn = driver.find_element_by_xpath("//label[@for='135738217_973017563']")
q8_btn.click()

#effort
#q8_btn = driver.find_element_by_xpath("//label[@for='135738217_973017564']")
#q8_btn.click()

#Exhilaration of music and image
#q8_btn = driver.find_element_by_xpath("//label[@for='135738217_973017565']")
#q8_btn.click()

#Other
#q8_btn = driver.find_element_by_xpath("//label[@for='135738217_973017566']")
#q8_btn.click()

time.sleep(1)

#question 9
#yes
q9_btn = driver.find_element_by_xpath("//label[@for='135738444_973019636']")
q9_btn.click()

#somehow
#q9_btn = driver.find_element_by_xpath("//label[@for='135738444_973019637']")
#q9_btn.click()

#no
#q9_btn = driver.find_element_by_xpath("//label[@for='135738444_973019638']")
#q9_btn.click()

time.sleep(1)

#question 10
#yes
q10_btn = driver.find_element_by_xpath("//label[@for='135738525_973020177']")
q10_btn.click()

#somehow
#q10_btn = driver.find_element_by_xpath("//label[@for='135738525_973020178']")
#q10_btn.click()

#no
#q10_btn = driver.find_element_by_xpath("//label[@for='135738525_973020179']")
#q10_btn.click()

time.sleep(1)

#question 11
#campain not appear to channel I use
q11_btn = driver.find_element_by_xpath("//label[@for='135738555_973021790']")
q11_btn.click()

#busy
#q11_btn = driver.find_element_by_xpath("//label[@for='135738555_973021791']")
#q11_btn.click()

#not interested
#q11_btn = driver.find_element_by_xpath("//label[@for='135738555_973021792']")
#q11_btn.click()

#other
#q11_btn = driver.find_element_by_xpath("//label[@for='135738555_973021793']")
#q11_btn.click()


time.sleep(1)

#question 12
#yes
q12_btn = driver.find_element_by_xpath("//label[@for='135738861_973022154']")
q12_btn.click()

#somehow
#q12_btn = driver.find_element_by_xpath("//label[@for='135738861_973022155']")
#q12_btn.click()

#no
#q12_btn = driver.find_element_by_xpath("//label[@for='135738861_973022156']")
#q12_btn.click()

time.sleep(1)

#question 13
q13_btn = driver.find_element_by_id('135739270-alternative')
q13_btn.send_keys("99")
time.sleep(1)
q131_btn = driver.find_element_by_id('question-title-135739270')
q131_btn.click()
time.sleep(1)

ok13_btn = driver.find_element_by_id('135739270-ok')
driver.execute_script("arguments[0].click();", ok13_btn)
time.sleep(3)


done_btn = driver.find_element_by_xpath("//button[@type='submit' and contains(., 'DONE')]")
driver.execute_script("arguments[0].click();", done_btn)
time.sleep(5)



driver.quit()