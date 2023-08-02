import pytest
import argparse
from selenium import webdriver

from pages.landing_page import LandingPage


@pytest.fixture()
def driver():
    # get the desired browser from the command line
    driver = get_driver()
    yield driver
    driver.close()


@pytest.fixture()
def landing_page(driver):
    return LandingPage(driver)


# the URL is the same for all tests
url = 'https://github.com/orgs/indigov-us/'


# Exercise #1
def test_num_repositories(driver, landing_page):
    driver.get(url)
    num_repos = landing_page.num_repos()

    assert num_repos == 17


# Get the browser to test against from the command line
def get_driver():
    parser = argparse.ArgumentParser(description='Test IndiGov GitHub')
    parser.add_argument('browser', help='The browser to test against: chrome or firefox')
    args = parser.parse_args()

    match args.browser:
        case 'chrome':
            driver = webdriver.Chrome()
        case 'firefox':
            driver = webdriver.Firefox()
        # additional browsers would go here
        case _:
            driver = webdriver.Chrome()

    return driver




