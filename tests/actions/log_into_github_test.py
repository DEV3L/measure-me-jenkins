from unittest.mock import call

from app.actions.log_into_github import LogIntoGitHub
from app.config import github_login_url, github_username, github_password


def test_log_into_github_execute(mock_browser_client):
    log_into_github = LogIntoGitHub(mock_browser_client)

    log_into_github.execute()

    mock_browser_client.get.assert_called_with(github_login_url)

    calls = [
        call(github_username, id='login_field'),
        call(github_password, id='password')
    ]

    mock_browser_client.set_text_value.assert_has_calls(calls)
    mock_browser_client.click_button.assert_called_with(name='commit')
