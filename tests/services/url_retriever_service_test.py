from app.services.url_retriever_service import UrlRetrieverService


def test_url_retriever_service_init(mock_web_driver):
    expected_url = 'url'
    expected_should_use_cache = True

    url_retriever_service = UrlRetrieverService(mock_web_driver, expected_url)

    assert mock_web_driver == url_retriever_service.web_driver
    assert expected_url == url_retriever_service.url
    assert expected_should_use_cache == url_retriever_service.should_use_cache


def test_get_without_cache(mock_web_driver):
    expected_url = 'url'
    expected_should_use_cache = False

    url_retriever_service = UrlRetrieverService(mock_web_driver, expected_url,
                                                should_use_cache=expected_should_use_cache)

    web_page = url_retriever_service.get()

    assert web_page == mock_web_driver.get.return_value
    assert expected_should_use_cache == url_retriever_service.should_use_cache
    mock_web_driver.get.assert_called_with(expected_url)
