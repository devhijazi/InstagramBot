from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot: 
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.driver = webdriver.Firefox(executable_path="./geckodriver/geckodriver-v0.29.1-linux64/geckodriver")

  def login(self):
    driver = self.driver
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    time.sleep(5)
    #//a[@href="/accounts/login/?source=auth_switcher"]
    #//input[@name="username]
    #//input[@name="password"]
    login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
    login_button.click()

    user_input = driver.find_element_by_xpath("//input[@name='username']")
    user_input.click()
    user_input.clear()
    user_input.send_keys(self.username)

    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.click()
    password_input.clear()
    password_input.send_keys(self.password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    self.pictures_comments("cars")


  @staticmethod
  def write_as_human(phrase, where_write):
    for word in phrase:
      where_write.send_keys(word)
      time.sleep(random.randint(1,5)/30)

  def pictures_comments(self, hashtag):
    driver = self.driver
    driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
    time.sleep(4)

    for i in range(1,3):
      driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
      time.sleep(5)

    hrefs = driver.find_elements_by_tag_name('a')
    pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
    [href for href in pic_hrefs if hashtag in href]
    print(hashtag + ' fotos ' + str(len(pic_hrefs)))

    for pic_href in pic_hrefs:
      driver.get(pic_href)
      driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

      try:
        coments_list = ["Toop!","Esse carro é foda demais","Lindo!","Bora @hijazi_gabriel","Braboo"]
        driver.find_element_by_class_name('Ypffh').click()
        textarea_input = driver.find_element_by_class_name('Ypffh')
        time.sleep(random.randint(2,8))
        self.write_as_human(random.choice(coments_list),textarea_input)
        time.sleep(random.randint(30,120))
        driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
        time.sleep(5)
      except Exception as e:
        print(e)
        time.sleep(5)


hjzBot = InstagramBot('arabesstg1','teste@123')
hjzBot.login()