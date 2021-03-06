from selenium.webdriver.common.by import By


def test_get_url(browser_client):
    expected_url = 'some_url'

    browser_client.get(expected_url)

    browser_client.web_driver.get.assert_called_with(expected_url)


def test_navigate_link(browser_client):
    expected_link_text = 'link_text'

    browser_client.navigate_link(expected_link_text)

    browser_client.web_driver.find_element_by_link_text.assert_called_with(expected_link_text)
    assert browser_client.web_driver.find_element_by_link_text.return_value.click.called


def test_set_text_field(browser_client):
    expected_element_id = 'element_id'
    expected_set_value = 'set_value'

    browser_client.set_text_value(expected_set_value, id=expected_element_id)

    browser_client.web_driver.find_element_by_id.assert_called_with(expected_element_id)
    browser_client.web_driver.find_element_by_id.return_value.send_keys.assert_called_with(expected_set_value)


def test_click_button(browser_client):
    expected_button_name = 'button'

    browser_client.click_button(name=expected_button_name)

    browser_client.web_driver.find_element_by_name.assert_called_with(expected_button_name)
    assert browser_client.web_driver.find_element_by_name.return_value.click.called


def test_find_elements_by_css_selector(browser_client):
    expected_css_selector = 'a.tip'

    elements = browser_client.find_elements_by_css_selector(expected_css_selector)

    browser_client.web_driver.find_elements.assert_called_with(By.CSS_SELECTOR, expected_css_selector)
    assert browser_client.web_driver.find_elements.return_value == elements


def test_find_element_by_class_name(browser_client):
    expected_class_name = 'class_name'

    element = browser_client.find_element_by_class_name(expected_class_name)

    browser_client.web_driver.find_element_by_class_name.assert_called_with(expected_class_name)
    assert browser_client.web_driver.find_element_by_class_name.return_value == element


def test_find_elements_by_tag_name(browser_client):
    expected_tag_name = 'tag_name'

    element = browser_client.find_elements_by_tag_name(expected_tag_name)

    browser_client.web_driver.find_elements_by_tag_name.assert_called_with(expected_tag_name)
    assert browser_client.web_driver.find_elements_by_tag_name.return_value == element
