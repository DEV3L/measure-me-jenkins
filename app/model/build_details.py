class BuildDetails:
    def __init__(self, *, branch_name: str, build_number: int,
                 queue_time: str = None, time: str = None, changes: list = None):
        self.branch_name = branch_name
        self.build_number = build_number
        self.queue_time = queue_time
        self.time = time
        self.changes = changes

    def __str__(self):
        return f'{self.branch_name},{self.build_number},{self.queue_time},{self.time},{self.changes}'
