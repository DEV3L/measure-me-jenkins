class BuildStatus:
    def __init__(self, *, branch_name: str, build_number: int, status: str = None, time: str = None):
        self.branch_name = branch_name
        self.build_number = build_number
        self.status = status
        self.time = time

    def __str__(self):
        return f'{self.branch_name},{self.build_number},{self.status},{self.time}'
