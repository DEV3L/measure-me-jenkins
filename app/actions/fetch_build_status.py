from app.actions._action import Action
from app.builders.build_status_builder import BuildStatusBuilder
from app.clients.browser_client import BrowserClient
from app.config import jenkins_url
from app.model.build_status import BuildStatus

base_console_url = f'{jenkins_url}view/OnShift-OnShift/job/OnShift-OnShift/job/'
console_css_class = 'console-output'


class FetchBuildStatus(Action):
    def __init__(self, browser_client: BrowserClient, branch_name: str, build_number: int):
        super().__init__(browser_client)
        self.branch_name = branch_name
        self.build_number = build_number

    @property
    def console_url(self) -> str:
        console_url = f'{base_console_url}{self.branch_name}/{self.build_number}/console'
        return console_url

    def execute(self) -> BuildStatus:
        self.browser_client.get(self.console_url)
        console_output_text = self.browser_client.find_element_by_class_name(console_css_class).text

        build_status_builder = BuildStatusBuilder(self.branch_name, self.build_number, console_output_text)
        build_status = build_status_builder.build()

        return build_status
