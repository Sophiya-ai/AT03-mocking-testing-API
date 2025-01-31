from HW import get_cat_image


def test_get_cat_image(mocker):
    mock_get = mocker.patch('HW.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        "id": "ebv",
        "url": "https://cdn2.thecatapi.com/images/ebv.jpg",
    }]

    image_url = get_cat_image()

    assert image_url == "https://cdn2.thecatapi.com/images/ebv.jpg"


def test_get_cat_image_with_error(mocker):
    mock_get = mocker.patch('HW.requests.get')
    mock_get.return_value.status_code = 404

    image_url = get_cat_image()

    assert image_url == None