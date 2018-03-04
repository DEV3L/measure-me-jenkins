from unittest.mock import MagicMock

from app.actions.fetch_build_status import FetchBuildStatus, console_css_class
from app.model.build_status import BuildStatus


def test_fetch_build_status_init(mock_browser_client):
    expected_branch_name = 'branch'
    expected_build_number = 1
    expected_console_url = f'http://jenkins-ci.route53.osstage.net:8080/view/OnShift-OnShift/job/OnShift-OnShift/job/' \
                           f'{expected_branch_name}/{expected_build_number}/console'

    fetch_build_status = FetchBuildStatus(mock_browser_client, expected_branch_name, expected_build_number)

    assert expected_branch_name == fetch_build_status.branch_name
    assert expected_build_number == fetch_build_status.build_number
    assert expected_console_url == fetch_build_status.console_url


def test_execute(mock_browser_client):
    expected_branch_name = 'branch'
    expected_build_number = 1

    console_logs = 'Finished: SUCCESS'
    mock_find_element_by_css_name_return_value = MagicMock()
    mock_find_element_by_css_name_return_value.text = console_logs

    mock_browser_client.find_element_by_class_name.return_value = mock_find_element_by_css_name_return_value

    expected_build_status = BuildStatus(branch_name=expected_branch_name, build_number=expected_build_number,
                                        status='Success')

    fetch_build_status = FetchBuildStatus(mock_browser_client, expected_branch_name, expected_build_number)

    build_output = fetch_build_status.execute()

    assert expected_build_status == build_output
    mock_browser_client.get.assert_called_with(fetch_build_status.console_url)
    mock_browser_client.find_element_by_class_name.assert_called_with(console_css_class)
