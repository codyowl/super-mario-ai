from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

game_url = "https://mario.xpixv.com/"

class Game:
	def __init__(self, game_url):
		self.game_url = game_url
		# launching the game on chrome with selenium
		self._driver = webdriver.Chrome(ChromeDriverManager().install())
		self._driver.get(game_url)
		time.sleep(5)
		self.actions = ActionChains(self._driver)

	def move_right(self):
		action_press_key_right_arrow = ActionChains(self._driver).key_down(Keys.ARROW_RIGHT)
		action_press_key_right_arrow_release = ActionChains(self._driver).key_up(Keys.ARROW_RIGHT)

		endtime = time.time() + 2.0

		while True:
			action_press_key_right_arrow.perform()

			if time.time() > endtime:
				action_press_key_right_arrow_release.perform()
				break

	def jump(self):
		action_key_down_w = ActionChains(self._driver).key_down(Keys.SPACE)
		action_key_up_w = ActionChains(self._driver).key_up(Keys.SPACE)

		endtime = time.time() + 1.0

		while True:
			action_key_down_w.perform()

			if time.time() > endtime:
				action_key_up_w.perform()
				break
			   

		
game = Game(game_url)

game.move_right()

game.jump()
time.sleep(5)

game.jump()
game.jump()
game.jump()
game.jump()
