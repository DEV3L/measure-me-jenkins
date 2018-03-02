from app.actions._action import Action
from app.builders.build_details_builder import BuildDetailsBuilder
from app.clients.browser_client import BrowserClient
from app.config import jenkins_url

base_console_url = f'{jenkins_url}view/OnShift-OnShift/job/OnShift-OnShift/job/'

page_headline_css = 'page-headline'
list_item_tag = 'li'


class FetchBuildDetails(Action):
    def __init__(self, browser_client: BrowserClient, branch_name: str, build_number: int):
        super().__init__(browser_client)
        self.branch_name = branch_name
        self.build_number = build_number

    @property
    def details_url(self):
        details_url = f'{base_console_url}{self.branch_name}/{self.build_number}/'
        return details_url

    def execute(self):
        self.browser_client.get(self.details_url)

        page_headline = self.browser_client.find_element_by_class_name(page_headline_css).text
        page_details = [detail.text for detail in self.browser_client.find_elements_by_tag_name(list_item_tag)]

        build_details_builder = BuildDetailsBuilder(self.branch_name, self.build_number, page_headline, page_details)
        build_details = build_details_builder.build()

        return build_details
