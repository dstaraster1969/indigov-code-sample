from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# The landing page for https://github.com/indigov-us is wildly different whether logged in or not
# For example, when logged in, the repositories header <a> has id="repositories-tab", but that
# id does not exist when not logged in. In real life, I'd create a test user and verify the
# logged in and logged out user experience. For this purpose, I'm just working with the
# not logged in page

class PageHeader:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # To get the number of repositories, I queried the button in the header rather than counting the repos.
    #
    def num_repos(self):
        repo_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab-item=org-header-repositories-tab]')
        repo_count_element = repo_tab.find_element(By.CLASS_NAME, 'js-profile-repository-count')

        # It takes a sec before the repo count is updated, so wait for it
        self.wait.until(lambda driver: repo_count_element.text != '')
        num_repos = repo_count_element.text

        return int(num_repos)

    def click_repo_tab(self):
        repo_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab-item=org-header-repositories-tab]')
        repo_tab.click()
