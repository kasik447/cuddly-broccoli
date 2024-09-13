# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/1/1.html')
#     fields = browser.find_elements(By.CLASS_NAME, 'form')
#     for i in fields:
#         i.send_keys('text')
#     button = browser.find_element(By.CLASS_NAME, 'btn')
#     button.click()
#     time.sleep(5)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/selenium/2/2.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     find_link = browser.find_element(By.LINK_TEXT, '16243162441624')
#     find_link.click()
#     result = browser.find_element(By.ID, 'result')
#     print(result.text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'http://parsinger.ru/selenium/3/3.html'
#
# count = 0
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     find_div = browser.find_elements(By.XPATH, "//div[@class='text']/p")
#     for i in find_div:
#         count += int(i.text)
#     print(count)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/selenium/3/3.html'
#
# count = 0
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     find_div = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
#     for i in find_div:
#         count += int(i.text)
#     print(count)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/selenium/4/4.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     checks = browser.find_elements(By.CLASS_NAME, 'check')
#     for i in checks:
#         i.click()
#     btn = browser.find_element(By.CLASS_NAME, 'btn')
#     btn.click()
#     print(browser.find_element(By.ID, 'result').text)
#     time.sleep(5)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/selenium/5/5.html'
#
# number = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
# 39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
# 74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
# 119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
# 154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
# 187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
# 208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
# 234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
# 256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
# 292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
# 318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
# 353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
# 419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
# 452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
# 480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
#
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     checks = browser.find_elements(By.CLASS_NAME, 'check')
#     for i in checks:
#         if int(i.get_attribute('value')) in number:
#             i.click()
#     btn = browser.find_element(By.CLASS_NAME, 'btn')
#     btn.click()
#     print(browser.find_element(By.ID, 'result').text)
#     time.sleep(5)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/selenium/7/7.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     count = 0
#     for i in browser.find_elements(By.TAG_NAME, 'option'):
#         count += int(i.text)
#     browser.find_element(By.ID, 'input_result').send_keys(count)
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     print(browser.find_element(By.ID, 'result').text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# url = 'https://parsinger.ru/selenium/6/6.html'
# n = ((12434107696 * 3) * 2) + 1
#
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     browser.find_element(By.TAG_NAME, 'select').send_keys(str(n))
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     print(browser.find_element(By.ID, 'result').text)

