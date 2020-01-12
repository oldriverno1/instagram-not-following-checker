from time import sleep

from selenium import webdriver


class instaBot():
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        # click login button
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(
            username)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(pw)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(2)
        # while True:
        #    pass

    def _get_names(self):  # scroll through scroll box and get text
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = []
        for name in links:
            if name.text != '':
                names.append(name.text)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return names

    def unfollwers(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(2)
        followers = self._get_names()
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        following = self._get_names()
        not_following = []
        for user in following:
            if user not in followers:
                not_following.append(user)
        print(f"there are {len(not_following)} users not following back, here's the list: {not_following}")


my_bot = instaBot('username', 'Password')  # input type == string
my_bot.unfollwers()
