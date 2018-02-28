from app.actions.fetch_build_details import FetchBuildDetails


def test_fetch_build_details_init(mock_browser_client):
    expected_branch_name = 'branch'
    expected_build_number = 1
    expected_console_url = f'http://jenkins-ci.route53.osstage.net:8080/view/OnShift-OnShift/job/OnShift-OnShift/job/' \
                           f'{expected_branch_name}/{expected_build_number}/'

    fetch_build_details = FetchBuildDetails(mock_browser_client, expected_branch_name, expected_build_number)

    assert expected_branch_name == fetch_build_details.branch_name
    assert expected_build_number == fetch_build_details.build_number
    assert expected_console_url == fetch_build_details.details_url

#
# def test_execute(mock_browser_client):
#     fetch_build_details = FetchBuildDetails(mock_browser_client, 'branch', 1)
#
#     build_details = fetch_build_details.execute()
#
#     assert mock_browser_client.find_element_by_class_name.return_value.text == build_details
#     mock_browser_client.get.assert_called_with(fetch_build_details.console_url, should_use_cache=True)
#     mock_browser_client.find_element_by_class_name.assert_called_with(console_css_class)
