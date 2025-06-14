FROM python:3.13-slim


WORKDIR  /app
COPY requirements/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
