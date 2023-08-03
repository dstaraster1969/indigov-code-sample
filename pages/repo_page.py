from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class RepoPage:
    def __init__(self, driver):
        self.driver = driver

    def clone_link(self):
        repo_code = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'get-repo')))
        repo_code.click()
        repo_modal = self.driver.find_element(By.CSS_SELECTOR, 'div[data-target="get-repo.modal"]')
        repo_input_group = repo_modal.find_element(By.CSS_SELECTOR, '.input-group')
        repo_input = repo_input_group.find_element(By.TAG_NAME, 'input')
        clone_link = repo_input.get_attribute('value')
        return clone_link
