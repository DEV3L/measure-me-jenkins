from app.actions.fetch_build_output import FetchBuildOutput, console_css_class


def test_fetch_build_output_init(mock_browser_client):
    expected_branch_name = 'branch'
    expected_build_number = 1
    expected_console_url = f'http://jenkins-ci.route53.osstage.net:8080/view/OnShift-OnShift/job/OnShift-OnShift/job/' \
                        f'{expected_branch_name}/{expected_build_number}/console'

    fetch_build_output = FetchBuildOutput(mock_browser_client, expected_branch_name, expected_build_number)

    assert expected_branch_name == fetch_build_output.branch_name
    assert expected_build_number == fetch_build_output.build_number
    assert expected_console_url == fetch_build_output.console_url


def test_execute(mock_browser_client):
    fetch_build_output = FetchBuildOutput(mock_browser_client, 'branch', 1)

    build_output = fetch_build_output.execute()

    assert mock_browser_client.find_element_by_class_name.return_value.text == build_output
    mock_browser_client.get.assert_called_with(fetch_build_output.console_url, should_use_cache=True)
    mock_browser_client.find_element_by_class_name.assert_called_with(console_css_class)
