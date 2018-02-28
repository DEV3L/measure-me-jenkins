from app.services.url_retriever_service import UrlRetrieverService, cache_dir
from app.transformers import transform_str


def test_url_retriever_service_init(mock_web_driver):
    expected_url = 'url'
    expected_url_hash = transform_str.sha_str(expected_url)
    expected_cache_file_path = cache_dir + expected_url_hash

    expected_should_use_cache = True

    url_retriever_service = UrlRetrieverService(mock_web_driver, expected_url)

    assert mock_web_driver == url_retriever_service.web_driver
    assert expected_url == url_retriever_service.url
    assert expected_url_hash == url_retriever_service.url_hash
    assert expected_cache_file_path == url_retriever_service.cache_file_path
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

# def test_is_url_cached_
