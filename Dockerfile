FROM python:3.9
WORKDIR /code/
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY main.py ./
CMD [ "python", "main.py" ]