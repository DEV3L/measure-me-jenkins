from app.actions.log_into_jenkins import LogIntoJenkins
from app.config import jenkins_url


def test_log_into_jenkins_execute(mock_browser_client):
    log_into_jenkis = LogIntoJenkins(mock_browser_client)

    log_into_jenkis.execute()

    mock_browser_client.get.assert_called_with(jenkins_url)
    mock_browser_client.navigate_link.assert_called_with('Log in')
