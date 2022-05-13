FROM python:3.9-slim-bullseye

# working directory.
WORKDIR /code

# copy requirements.txt
COPY requirements.txt /code/

# Install requirements.txt
RUN pip install -r requirements.txt

# Get the code.
COPY . /code/

# Expose the port 
EXPOSE 5000

# Define the run command for the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]