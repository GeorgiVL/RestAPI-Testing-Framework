FROM python:3.9

WORKDIR /PycharmProjects/restapi_testing_fwm
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /PycharmProjects/restapi_testing_fwm


