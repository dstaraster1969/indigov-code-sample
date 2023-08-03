import sys
from time import sleep

import pytest
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.landing_page import LandingPage
# from pages.repo_page import RepoPage


@pytest.fixture()
def driver():
    # Hardcoding browser; irl would implement cross-browser testing
    driver = webdriver.Chrome()
    driver.get('https://github.com/orgs/indigov-us/')
    yield driver
    driver.close()


# Exercise #1
def test_num_repositories(driver):
    num_repos = LandingPage(driver).num_repos()

    assert num_repos == 17


def test_language_filter(driver):
    filter_on_language(driver, 'typescript')


def filter_on_language(driver, language):
    repo_tab = driver.find_element(By.CSS_SELECTOR, '[data-tab-item=org-header-repositories-tab]')
    repo_tab.click()
    language_options = driver.find_element(By.ID, 'language-options')
    language_button = language_options.find_element(By.CSS_SELECTOR, '.btn')
    language_button.click()

    # after clicking on the Language button, the language_options element is stale
    # so re-find it
    language_options = driver.find_element(By.ID, 'language-options')
    language_option = language_options.find_element(By.ID, f'language_{language}')
    language_option_parent = language_option.find_element(By.XPATH, '..')
    language_option_parent.click()
    sleep(5)



