from unittest.mock import MagicMock

from pytest import fixture

from app.clients.browser_client import BrowserClient


@fixture(name='browser_client')
def _browser_client(mock_web_driver):
    browser_client = BrowserClient(mock_web_driver)
    assert mock_web_driver == browser_client.web_driver

    return browser_client


@fixture(name='mock_browser_client')
def _mock_browser_client():
    browser_client = MagicMock()
    return browser_client


@fixture(name='mock_web_driver')
def _mock_web_driver():
    mock_web_driver = MagicMock()
    return mock_web_driver
