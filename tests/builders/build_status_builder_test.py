from app.builders.build_status_builder import BuildStatusBuilder
from app.model.build_status import BuildStatus
from pytest import fixture

expected_branch_name = 'branch'
expected_build_number = 1
expected_build_log = 'build_log'


@fixture(name='build_status_builder')
def _build_status_builder():
    build_status_builder = BuildStatusBuilder(expected_branch_name, expected_build_number, expected_build_log)

    assert expected_branch_name == build_status_builder.branch_name
    assert expected_build_number == build_status_builder.build_number
    assert expected_build_log == build_status_builder.build_log

    return build_status_builder


def test_build_failure_default(build_status_builder):
    expected_status = 'Failure'

    build_status = build_status_builder.build()

    assert BuildStatus == type(build_status)
    assert expected_branch_name == build_status.branch_name
    assert expected_build_number == build_status.build_number
    assert expected_status == build_status.status


def test_build_success_in_log(build_status_builder):
    expected_status = 'Success'

    build_log = 'Finished: SUCCESS'
    build_status_builder.build_log = build_log

    build_status = build_status_builder.build()

    assert expected_status == build_status.status
