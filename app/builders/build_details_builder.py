class BuildDetailsBuilder:
    def __init__(self, branch_name: str, build_number: int, page_headline: str, page_details: list):
        self.branch_name = branch_name
        self.build_number = build_number
        self.page_headline = page_headline
        self.page_details = page_details

    def build(self):
        pass
