from selenium.webdriver.remote.webdriver import WebDriver

cache_dir = './data/pickle/web_pages/'


class UrlRetrieverService:
    def __init__(self, web_driver: WebDriver, url: str, *, should_use_cache=True):
        self.web_driver = web_driver
        self.url = url
        self.should_use_cache = should_use_cache

    def get(self):
        return self.web_driver.get(self.url)
