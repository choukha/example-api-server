import requests


def test_infer_route():
    sample_request = {"X": [[1, 2, 3], [4, 5, 6]]}
    expected_response = {"Y": [[2.03701, 2.345], [5.739376, 6.0338]]}
    response = requests.post("http://127.0.0.1:8000/infer", json=sample_request)
    assert expected_response == response.json()
