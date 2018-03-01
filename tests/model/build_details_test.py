from app.model.build_details import BuildDetails


def test_build_details_init():
    expected_branch_name = 'branch_name'
    expected_build_number = 1
    expected_start_time = 'Feb 28, 2018 3:10:34 PM'
    expected_queue_time = '3 ms'
    expected_total_time = '47 m'
    expected_changes = ['changes']

    expected_build_details_str = 'branch_name,1,Feb 28, 2018 3:10:34 PM,3 ms,47 m,[\'changes\']'

    build_details = BuildDetails(
        branch_name=expected_branch_name,
        build_number=expected_build_number,
        start_time=expected_start_time,
        queue_time=expected_queue_time,
        total_time=expected_total_time,
        changes=['changes']
    )

    assert expected_branch_name == build_details.branch_name
    assert expected_build_number == build_details.build_number
    assert expected_start_time == build_details.start_time
    assert expected_queue_time == build_details.queue_time
    assert expected_total_time == build_details.total_time
    assert expected_changes == build_details.changes
    assert expected_build_details_str == str(build_details)
