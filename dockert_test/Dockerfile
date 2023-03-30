FROM python:3.10

WORKDIR /test_api

COPY ./requirements.txt ./
RUN pip install requirements.txt
COPY ./src ./src



CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "-reload"]
