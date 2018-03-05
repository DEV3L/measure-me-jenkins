class BuildDetails:
    def __init__(self, *, branch_name: str, build_number: int, start_time: str = None,
                 queue_time: float = None, total_time: float = None, changes: list = None):
        self.branch_name = branch_name
        self.build_number = build_number
        self.start_time = start_time
        self.queue_time = queue_time
        self.total_time = total_time
        self.changes = changes

    def __str__(self):
        return f'{self.branch_name}|{self.build_number}|' \
               f'{self.start_time}|{self.queue_time}|{self.total_time}|{self.changes}'

    def __eq__(self, other):
        return str(self) == str(other)
