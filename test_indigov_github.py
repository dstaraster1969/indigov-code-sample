import pytest
from selenium import webdriver

from pages.landing_page import PageHeader
from pages.repo_page import RepoPage
from pages.repos_page import ReposPage


# The logged in DOM is different from the not logged in DOM. This tests the not logged in pages. For a real project,
# a test user would be created, and both scenarios would be tested.

# Use a fixture to instantiate the webdriver. This way the setup is done on every test, and the driver is closed after
# each test. This allows each test to begin in a clean state.
@pytest.fixture()
def driver():
    # Hardcoded the browser. In a real project, multiple browsers would be allowed and tests would be run
    # against each of them.
    driver = webdriver.Chrome()
    driver.get('https://github.com/orgs/indigov-us/')
    yield driver
    driver.close()


# Exercise #1
def test_num_repositories(driver):
    num_repos = PageHeader(driver).num_repos()

    assert num_repos == 17


# Exercise #2
def test_language_filter(driver):
    repo_page = ReposPage(driver)
    repo_page.filter_on_language('typescript')
    num_repos = repo_page.num_filtered_repos()

    assert int(num_repos) == 5


# Exercise #3
def test_sort(driver):
    repo_page = ReposPage(driver)
    repo_page.sort_repos('name')
    num_repos = PageHeader(driver).num_repos()
    first_repo_name = repo_page.repo_at_index_text(0)
    middle_repo_name = repo_page.repo_at_index_text(6)
    last_repo_name = repo_page.repo_at_index_text(num_repos - 1)

    # Generally, multiple asserts in one testcase are a bad idea. Here, though, all the asserts are testing the
    # same thing.
    assert 'ansible' in first_repo_name
    assert 'indigov' in middle_repo_name
    assert 'zendesk-client-api' in last_repo_name


# Exercise #4
def test_clone_link(driver):
    repos_page = ReposPage(driver)
    repos_page.sort_repos('name')
    num_repos = PageHeader(driver).num_repos()
    repos_page.select_repo_at_index(num_repos - 1)
    clone_link = RepoPage(driver).clone_link()

    assert clone_link == 'https://github.com/indigov-us/zendesk-client-api.git'




