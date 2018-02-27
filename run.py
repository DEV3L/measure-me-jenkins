from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver

from app.actions.fetch_build_numbers_for_branch import FetchBuildNumbersForBranch
from app.actions.fetch_build_output import FetchBuildOutput
from app.actions.log_into_github import LogIntoGitHub
from app.actions.log_into_jenkins import LogIntoJenkins
from app.builders.build_status_builder import BuildStatusBuilder
from app.clients.browser_client import BrowserClient


def _run(chrome_web_driver: ChromeWebDriver()):
    browser_client = BrowserClient(chrome_web_driver)

    log_into_github = LogIntoGitHub(browser_client)
    log_into_github.execute()

    log_into_jenkins = LogIntoJenkins(browser_client)
    log_into_jenkins.execute()

    fetch_build_information_for_branch = FetchBuildNumbersForBranch(browser_client, 'master')
    build_numbers = fetch_build_information_for_branch.execute()

    build_statuses = []

    for build_number in build_numbers:
        fetch_build_output = FetchBuildOutput(browser_client, 'master', build_number)
        build_output = fetch_build_output.execute()

        build_status_builder = BuildStatusBuilder('master', build_number, build_output)
        build_statuses.append(build_status_builder.build())


    for build_status in build_statuses:
        print(build_status)

if __name__ == '__main__':
    chrome_web_driver = ChromeWebDriver()
    try:
        _run(chrome_web_driver)
    except:
        chrome_web_driver.close()
    else:
        chrome_web_driver.close()
