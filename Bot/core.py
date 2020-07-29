from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import sys
import time
import os


class InstagramBot():
	"""
	Automatically log in to Instagram, auto close the noticements etc.
	"""
	global followers, following, inter

	followers = []
	following = []
	inter = []

	def __init__(self, email, password):
		self.__driver_path = "YOUR_PATH"
		self.options = webdriver.ChromeOptions()
		self.maximized = self.options.add_argument("start-maximized")
		self.browser = webdriver.Chrome(executable_path = self.__driver_path, options = self.options)
		self.__email = email
		self.__password = password

	def signIn(self):
		
		self.browser.get("https://www.instagram.com/accounts/login/")
		time.sleep(2)

		emailInput = self.browser.find_elements_by_css_selector("form input")[0]
		passwordInput = self.browser.find_elements_by_css_selector("form input")[1]

		emailInput.send_keys(self.__email)
		passwordInput.send_keys(self.__password)
		passwordInput.send_keys(Keys.ENTER)

		time.sleep(4)
		self.browser.get("https://www.instagram.com/" + self.__email)
		time.sleep(2)
		
	def closeBrowser(self):
		self.browser.close()

	def unfUser(self, username, slow_mode = True):
		self.browser.get(username)
		try:
			unfollowButton = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
			unfollowButton.click()

			confirmButton = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")
			confirmButton.click()
			self.pbar.update()
			if not slow_mode:
				time.sleep(1)

			if slow_mode:
				time.sleep(4)

			self.pbar.refresh()

		except:
			print("Hata")

	def intersection(self, l1, l2):
		inter = [x for x in l1 if x in l2]
		self.pbar = tqdm(total=len(inter))
		return inter

	def getUserFollowers(self):

		nn = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
		followersLink = self.browser.find_elements_by_css_selector('ul li a')[0]
		followersLink.click()
		time.sleep(2)

		followersList = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div')
		numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
		followersList.click()
		time.sleep(2)

		total_num = int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text)

		actionChain = webdriver.ActionChains(self.browser)

		while (numberOfFollowersInList <( total_num -2 )):	

			actionChain.key_down(Keys.TAB).key_up(Keys.TAB).perform()
			numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
			sys.stdout.write("\r"+ str(total_num) + "/" + str(numberOfFollowersInList) )
			sys.stdout.flush()
		
		for followinguser in followersList.find_elements_by_css_selector('li'):
			followinguserLink = followinguser.find_element_by_css_selector('a').get_attribute('href')
			followers.append(followinguserLink)
			if (len(followers) == total_num):
				break

		return followers

	def getFollowing(self):

		followingLink = self.browser.find_elements_by_css_selector('ul li a')[1]
		followingLink.click()
		time.sleep(2)

		followingList = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div')
		numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))

		followingList.click()
		time.sleep(2)

		total_num = int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text)
		
		actionChain = webdriver.ActionChains(self.browser)

		while (numberOfFollowingInList <( total_num - 4)):	

			actionChain.key_down(Keys.TAB).key_up(Keys.TAB).perform()
			numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))
			sys.stdout.write("\r"+ str(total_num) + "/" + str(numberOfFollowingInList) )
			sys.stdout.flush()
		
		for user in followingList.find_elements_by_css_selector('li'):
			userLink = user.find_element_by_css_selector('a').get_attribute('href')
			following.append(userLink)
			if (len(following) == total_num):
				break

		return following


