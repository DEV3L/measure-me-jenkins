from app.model.build_status import BuildStatus


class BuildStatusBuilder:
    def __init__(self, branch_name:str, build_number:int, build_log: str):
        self.branch_name = branch_name
        self.build_number = build_number
        self.build_log = build_log

    def build(self):
        build_status = BuildStatus(branch_name=self.branch_name,
                                   build_number=self.build_number,
                                   status='Failure')

        if 'Finished: SUCCESS' in self.build_log:
            build_status.status = 'Success'
        return build_status
