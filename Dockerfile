# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./note_server /code/note_server

# uvicorn note_server.main:app --host 0.0.0.0 --port 9000
CMD ["uvicorn", "note_server.main:app", "--host", "0.0.0.0", "--port", "9000"]