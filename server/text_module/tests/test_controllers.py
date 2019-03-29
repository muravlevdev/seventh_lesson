from text_module.controllers import (
    get_upper_text, get_lower_text
)


def test_get_upper_text():
    TEST_TEXT_UPPER = 'test text'
    ASSERT_TEXT_UPPER = 'TEST TEXT'
    assert get_upper_text(TEST_TEXT_UPPER) == ASSERT_TEXT_UPPER


def test_get_lower_text():
    TEST_TEXT_LOWER = 'TEST TEXT'
    ASSERT_TEXT_LOWER = 'test text'
    assert get_lower_text(TEST_TEXT_LOWER) == ASSERT_TEXT_LOWER