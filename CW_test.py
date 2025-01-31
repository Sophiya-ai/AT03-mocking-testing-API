# import pytest , также импортируем pytest-mock
from CW import get_weather


# Mocker — это фикстура, которая предоставляется модулем Pytest mock.
# Эта фикстура позволяет мокировать объекты и различные функции

# Используем patch, чтобы изменить поведение функции get, прописанной в CW.py.
# Для этого создадим переменную mock_get и мокируем (меняем поведение) у функции request_get.
# Таким образом мы заменили функцию на mock-объект, с которым можно работать.
# Мы можем поменять значение, которое выдается после получения через функцию get.
# Добавим информацию внутри фигурных скобок: погоду и список с описанием
def test_get_weather(mocker):
    mock_get = mocker.patch('CW.requests.get')

    # Прописываем mock-объект, с помощью return меняя возвращаемое значение,
    # а также указываем, что за значение мы меняем — это статус-код
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.5}
    }

    api_key = '0ca1c2a94cf6c7789b050e71c83b0999'
    town = 'London'

    weather_data = get_weather(api_key, town)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.5}
    }


def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('CW.requests.get')
    mock_get.return_value.status_code = 404

    api_key = '0ca1c2a94cf6c7789b050e71c83b0999'
    town = 'London'

    weather_data = get_weather(api_key, town)

    assert weather_data == None