from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ReposPage:
    def __init__(self, driver):
        self.driver = driver

    def filter_on_language(self, language):
        wait = WebDriverWait(self.driver, 10)
        repo_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab-item=org-header-repositories-tab]')
        repo_tab.click()
        wait.until(EC.url_contains('repositories'))
        language_options = self.driver.find_element(By.ID, 'language-options')

        # I tried several expected conditions to wait on, and none worked.
        # sleep() is not ideal, but it is 100% consistent
        sleep(1)
        language_button = language_options.find_element(By.CSS_SELECTOR, '.btn')
        language_button.click()
        language_options = self.driver.find_element(By.ID, 'language-options')
        language_option = language_options.find_element(By.ID, f'language_{language}')
        language_option_parent = language_option.find_element(By.XPATH, '..')
        language_option_parent.click()
        sleep(2)

    def sort_repos(self, sort_type):
        wait = WebDriverWait(self.driver, 10)
        repo_tab = self.driver.find_element(By.CSS_SELECTOR, '[data-tab-item=org-header-repositories-tab]')
        repo_tab.click()
        wait.until(EC.url_contains('repositories'))
        sort_options = self.driver.find_element(By.ID, 'sort-options')

        # I tried several expected conditions to wait on, and none worked.
        # sleep() is not ideal, but it is 100% consistent
        sleep(1)
        sort_button = sort_options.find_element(By.CSS_SELECTOR, '.btn')

        # In this case, which should be virtually identical to filter_on_language(), but
        # this click displays the menu.
        sort_button.click()
        sort_options = self.driver.find_element(By.ID, 'sort-options')
        sort_option = sort_options.find_element(By.ID, f'sort_{sort_type}')
        sort_option_parent = sort_option.find_element(By.XPATH, '..')
        sort_option_parent.click()
        sleep(2)

    def num_filtered_repos(self):
        repos = self.driver.find_element(By.ID, 'org-repositories')
        return repos.find_element(By.TAG_NAME, 'strong').text

    def repo_at_index_text(self, i):
        repo = self.repo_at_index(i)
        link = repo.find_element(By.TAG_NAME, 'a')
        return link.text.strip()

    def repo_at_index(self, i):
        repo_list = self.driver.find_element(By.CSS_SELECTOR, '.org-repos.repo-list')
        repos = repo_list.find_elements(By.TAG_NAME, 'li')
        repo = repos[i]

        return repo

    def select_repo_at_index(self, i):
        repo = self.repo_at_index(i)
        link = repo.find_element(By.TAG_NAME, 'a')
        link.click()
