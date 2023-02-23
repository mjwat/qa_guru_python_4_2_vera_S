from selene import be, have
from selene.api import *


search_input = s('[name="q"]')

search_with_result = s('#search')
search_without_result = s('#topstuff div div p:first-child')

successful_request_string = 'yashaka/selene'
successful_result_output = 'Selene - User-oriented Web UI browser tests in Python'

unsuccessful_request_string = 'lkjhgfdsaqwertyuiopmnbvcxzlkjhgfdsaqwertyuiopmnbvcxz'
unsuccessful_result_output = 'По запросу ' + unsuccessful_request_string + ' ничего не найдено.'


def test_successful_search(open_google):
    search_input.should(be.blank).type(successful_request_string).press_enter()
    assert search_with_result.should(have.text(successful_result_output))


def test_unsuccessful_search(open_google):
    search_input.should(be.blank).type(unsuccessful_request_string).press_enter()
    search_without_result.should(have.text(unsuccessful_result_output))
