from app.model.build_details import BuildDetails
from app.services.parse_string_time import parse_string_time


class BuildDetailsBuilder:
    def __init__(self, branch_name: str, build_number: int, page_headline: str, page_details: list):
        self.branch_name = branch_name
        self.build_number = build_number
        self.page_headline = page_headline
        self.page_details = page_details

    def build(self):
        build_details = BuildDetails(branch_name=self.branch_name, build_number=self.build_number)
        build_details.start_time = self._extract_start_time()
        self._set_build_details_using_page_details(build_details)

        return build_details

    def _extract_start_time(self):
        start_time = self.page_headline[self.page_headline.index('(') + 1: self.page_headline.index(')')]
        return start_time

    def _set_build_details_using_page_details(self, build_details: BuildDetails):
        changes = []

        _page_details = [detail for detail in self.page_details if detail]
        for detail in _page_details:
            if 'total' in detail:
                build_details.total_time = self._extract_time(detail, 'total')
            elif 'waiting' in detail:
                build_details.queue_time = self._extract_time(detail, 'waiting')
            elif '(detail / githubweb)' in detail:
                changes.append(detail[:detail.index('(detail / githubweb)') - 1])

        build_details.changes = changes

    @staticmethod
    def _extract_time(detail: str, index_keyword: str):
        time_str = detail[:detail.index(index_keyword) - 1]
        time = parse_string_time(time_str)
        return time
