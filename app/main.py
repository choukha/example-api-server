# Library Imports
from os.path import dirname, join, realpath

import numpy as np
import uvicorn
from fastapi import FastAPI

# Import schemas
from app.schemas import RequestModel, ResponseModel

# path for model coefficients file
MODEL_WEIGHTS_PATH = join(dirname(realpath(__file__)), "model_weights", "model.csv")

# Instance of API, this will be used in command when running the server
app = FastAPI(
    title="ML_Pred_API",
    description="API to get the model predictions/output for a list of inputs",
    version="0.0.1",
)

# Create "infer" endpoint/path
@app.post("/infer", tags=["ML Model Inference"], response_model=ResponseModel)
def predict(x: RequestModel) -> ResponseModel:
    """Inference Function for getting output from Model
        y = Ax
        where A is the coefficient matrix obtained using Machine learning.

    Args:
        x (RequestModel): List of Input Arrays

    Returns:
        y (ResponseModel): List of Output Arrays
    """
    # Get the x array
    x_array = np.asarray(x.X)
    # Load the coefficient matrix from csv file
    A = np.loadtxt(MODEL_WEIGHTS_PATH, skiprows=0, delimiter=",")
    # calculate y=Ax
    y = np.dot(A, x_array.T).T.tolist()
    return {"Y": y}


# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
