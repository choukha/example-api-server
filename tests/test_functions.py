from app.main import predict
from app.schemas import RequestModel, ResponseModel


def test_predict_calculation():
    sample_request = RequestModel()
    sample_request.X = [[1, 2, 3], [4, 5, 6]]
    expected_response = ResponseModel()
    expected_response.Y = [[2.03701, 2.345], [5.739376, 6.0338]]
    assert predict(sample_request) == expected_response
