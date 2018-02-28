from selenium.webdriver.remote.webdriver import WebDriver

from app.transformers import transform_str

cache_dir = './data/pickle/web_pages/'


class UrlRetrieverService:
    def __init__(self, web_driver: WebDriver, url: str, *, should_use_cache=True):
        self.web_driver = web_driver
        self.url = url
        self.should_use_cache = should_use_cache

    @property
    def url_hash(self):
        return transform_str.sha_str(self.url)

    @property
    def cache_file_path(self):
        return f'{cache_dir}{self.url_hash}'

    def get(self):
        if not self.should_use_cache:
            return self.web_driver.get(self.url)

        # try:
        #     web_page = load_pickle_data()
        # except FileNotFoundError:
        #     web_page = self.web_driver.get(self.url)
