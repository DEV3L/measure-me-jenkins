from app.builders.build_details_builder import BuildDetailsBuilder
from app.model.build_details import BuildDetails


def test_build_details_builder():
    expected_branch_name = 'branch'
    expected_build_number = 1
    expected_page_headline = 'Build #87-PROD-GREEN (Feb 21, 2018 2:45:29 PM)'
    expected_page_details = ['', 'commit message (detail / githubweb)', '2 ms waiting in the queue;',
                             '40 min building on an executor;', '40 min total from scheduled to completion.', 'master']

    expected_build_details = BuildDetails(branch_name=expected_branch_name, build_number=expected_build_number,
                                          start_time='Feb 21, 2018 2:45:29 PM', queue_time=.002, total_time=2400.0,
                                          changes=['commit message'])

    build_details_builder = BuildDetailsBuilder(expected_branch_name, expected_build_number,
                                                expected_page_headline, expected_page_details)
    build_details = build_details_builder.build()

    assert str(expected_build_details) == str(build_details)
    assert expected_build_details == build_details
