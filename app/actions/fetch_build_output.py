from app.actions._action import Action
from app.clients.browser_client import BrowserClient
from app.config import jenkins_url

base_console_url = f'{jenkins_url}view/OnShift-OnShift/job/OnShift-OnShift/job/'
console_css_class = 'console-output'

class FetchBuildOutput(Action):
    def __init__(self, browser_client: BrowserClient, branch_name: str, build_number: int):
        super().__init__(browser_client)
        self.branch_name = branch_name
        self.build_number = build_number

    @property
    def console_url(self):
        console_url = f'{base_console_url}{self.branch_name}/{self.build_number}/console'
        return console_url

    def execute(self):
        self.browser_client.get(self.console_url)
        console_output_text = self.browser_client.find_element_by_class_name(console_css_class).text
        return console_output_text
