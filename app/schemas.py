# Schemas
from typing import List

from pydantic import BaseModel


class RequestModel(BaseModel):
    """
    Request Body
    List of Input vector containing following fields in the order:
    1. Pressure [Pa]
    2. Temperature [∘C]
    3. Efficiency Factor [1]

    """

    X: List[List[float]] = [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]


class ResponseModel(BaseModel):
    """
    Response from API
    List of Output vectors containing following fields in the order:
    1. Power Consumption [kW]
    2. Production Rate [kg/s]

    """

    Y: List[List[float]] = [[2.03, 2.3], [2.03, 2.3]]
