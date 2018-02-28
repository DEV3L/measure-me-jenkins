from unittest.mock import patch, MagicMock

from pytest import fixture

from app.services.url_retriever_service import UrlRetrieverService, cache_dir
from app.transformers import transform_str


@fixture(name='url_retriever_service')
def _url_retriever_service(mock_web_driver):
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

    return url_retriever_service


def test_get_without_cache(mock_web_driver):
    expected_url = 'url'
    expected_should_use_cache = False

    url_retriever_service = UrlRetrieverService(mock_web_driver, expected_url,
                                                should_use_cache=expected_should_use_cache)

    web_page = url_retriever_service.get()

    assert web_page == mock_web_driver.get.return_value
    assert expected_should_use_cache == url_retriever_service.should_use_cache
    mock_web_driver.get.assert_called_with(expected_url)


@patch('app.services.url_retriever_service.load_pickle_data')
def test_get_url_cached(mock_load_pickle_data, url_retriever_service):
    web_page = url_retriever_service.get()

    assert mock_load_pickle_data.return_value == web_page
    mock_load_pickle_data.assert_called_with(url_retriever_service.cache_file_path)


@patch('app.services.url_retriever_service.load_pickle_data')
def test_get_url_not_cached(mock_load_pickle_data, url_retriever_service):
    url_retriever_service._write_pickle_data = MagicMock()
    mock_load_pickle_data.side_effect = FileNotFoundError()

    web_page = url_retriever_service.get()

    assert url_retriever_service.web_driver.get.return_value == web_page
    url_retriever_service._write_pickle_data.assert_called_with(web_page)
    mock_load_pickle_data.assert_called_with(url_retriever_service.cache_file_path)


@patch('app.services.url_retriever_service.serialize')
@patch('app.services.url_retriever_service.write_pickle_data')
def test_write_pickle_data(mock_write_pickle_data, mock_serialize, url_retriever_service):
    expected_web_page = 'web_page'

    url_retriever_service._write_pickle_data(expected_web_page)

    mock_serialize.assert_called_with(expected_web_page)
    mock_write_pickle_data.assert_called_with(mock_serialize.return_value, url_retriever_service.cache_file_path)
