from unittest.mock import patch, MagicMock

from app.actions.fetch_build_details import FetchBuildDetails, page_headline_css, list_item_tag


def test_fetch_build_details_init(mock_browser_client):
    expected_branch_name = 'branch'
    expected_build_number = 1
    expected_console_url = f'http://jenkins-ci.route53.osstage.net:8080/view/OnShift-OnShift/job/OnShift-OnShift/job/' \
                           f'{expected_branch_name}/{expected_build_number}/'

    fetch_build_details = FetchBuildDetails(mock_browser_client, expected_branch_name, expected_build_number)

    assert expected_branch_name == fetch_build_details.branch_name
    assert expected_build_number == fetch_build_details.build_number
    assert expected_console_url == fetch_build_details.details_url


@patch('app.actions.fetch_build_details.BuildDetailsBuilder')
def test_execute(mock_build_details_builder, mock_browser_client):
    mock_page_headline = MagicMock()
    mock_page_details = [MagicMock()]

    mock_browser_client.find_element_by_class_name.return_value = mock_page_headline
    mock_browser_client.find_elements_by_tag_name.return_value = mock_page_details

    fetch_build_details = FetchBuildDetails(mock_browser_client, 'branch', 1)

    build_details = fetch_build_details.execute()

    assert mock_build_details_builder.return_value.build.return_value == build_details
    mock_browser_client.get.assert_called_with(fetch_build_details.details_url)
    mock_browser_client.find_element_by_class_name.assert_called_with(page_headline_css)
    mock_browser_client.find_elements_by_tag_name.assert_called_with(list_item_tag)
    mock_build_details_builder.assert_called_with(
        fetch_build_details.branch_name,
        fetch_build_details.build_number,
        mock_page_headline.text,
        [detail.text for detail in mock_page_details]
    )
