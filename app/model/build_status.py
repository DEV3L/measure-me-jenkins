class BuildStatus:
    def __init__(self, *, branch_name: str, build_number: int, status: str = None):
        self.branch_name = branch_name
        self.build_number = build_number
        self.status = status

    def __str__(self):
        return f'{self.branch_name}|{self.build_number}|{self.status}'

    def __eq__(self, other):
        return str(self) == str(other)
