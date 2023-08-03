import sys
from time import sleep

import pytest
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.landing_page import PageHeader
from pages.repo_page import RepoPage
from pages.repos_page import ReposPage


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
    num_repos = PageHeader(driver).num_repos()

    assert num_repos == 17


def test_language_filter(driver):
    repo_page = ReposPage(driver)
    repo_page.filter_on_language('typescript')
    num_repos = repo_page.num_filtered_repos()

    assert int(num_repos) == 5


def test_sort(driver):
    repo_page = ReposPage(driver)
    repo_page.sort_repos('name')
    num_repos = PageHeader(driver).num_repos()
    first_repo_name = repo_page.repo_at_index_text(0)
    last_repo_name = repo_page.repo_at_index_text(num_repos - 1)

    assert 'ansible' in first_repo_name
    assert 'zendesk-client-api' in last_repo_name


def test_clone_link(driver):
    repos_page = ReposPage(driver)
    repos_page.sort_repos('name')
    num_repos = PageHeader(driver).num_repos()
    repos_page.select_repo_at_index(num_repos - 1)
    clone_link = RepoPage(driver).clone_link()

    assert clone_link == 'https://github.com/indigov-us/zendesk-client-api.git'




