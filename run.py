from logging import getLogger

from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver

from app.actions.fetch_build_details import FetchBuildDetails
from app.actions.fetch_build_numbers_for_branch import FetchBuildNumbersForBranch
from app.actions.fetch_build_status import FetchBuildStatus
from app.actions.log_into_github import LogIntoGitHub
from app.actions.log_into_jenkins import LogIntoJenkins
from app.clients.browser_client import BrowserClient

logger = getLogger(__name__)
branch_name = 'master'


def _run(chrome_web_driver: ChromeWebDriver()):
    browser_client = BrowserClient(chrome_web_driver)

    log_into_github = LogIntoGitHub(browser_client)
    log_into_github.execute()

    log_into_jenkins = LogIntoJenkins(browser_client)
    log_into_jenkins.execute()

    fetch_build_information_for_branch = FetchBuildNumbersForBranch(browser_client, branch_name)
    build_numbers = fetch_build_information_for_branch.execute()

    build_status_list = []
    build_details_list = []

    for build_number in build_numbers:
        fetch_build_status = FetchBuildStatus(browser_client, branch_name, build_number)
        build_status = fetch_build_status.execute()
        build_status_list.append(build_status)

        fetch_build_details = FetchBuildDetails(browser_client, branch_name, build_number)
        build_details = fetch_build_details.execute()
        build_details_list.append(build_details)

    print('branch|build number|status|branch|build number|start time|queue time|total time|changes')

    for build_details, build_status in zip(build_details_list, build_status_list):
        print(f'{build_status}|{build_details}')


if __name__ == '__main__':
    chrome_web_driver = ChromeWebDriver()
    try:
        _run(chrome_web_driver)
    except Exception as e:
        logger.exception(e)
        chrome_web_driver.close()
    else:
        chrome_web_driver.close()
