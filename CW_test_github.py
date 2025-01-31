from CW_github import github_user


def test_github_user(mocker):
    mock_get = mocker.patch('CW_github.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'niz',
        'id': 12345,
        'name': 'Nina'
    }
    user_data = github_user('niz')
    assert user_data == {
        'login': 'niz',
        'id': 12345,
        'name': 'Nina'
    }


def test_github_user_with_error(mocker):
    mock_get = mocker.patch('CW_github.requests.get')
    mock_get.return_value.status_code = 500

    user_data = github_user('niz')
    assert user_data == None
