from app.model.build_status import BuildStatus


def test_build_status_init():
    expected_branch_name = 'branch_name'
    expected_build_number = 1
    expected_status = 'pass'

    expected_build_status_str = 'branch_name,1,pass'

    build_status = BuildStatus(
        branch_name=expected_branch_name,
        build_number=expected_build_number,
        status=expected_status
    )

    assert expected_branch_name == build_status.branch_name
    assert expected_build_number == build_status.build_number
    assert expected_status == build_status.status
    assert expected_build_status_str == str(build_status)
