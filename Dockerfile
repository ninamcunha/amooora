FROM python:3.10.6-slim

# We strip the requirements from useless packages like `ipykernel`, `matplotlib` etc...
COPY requirements_prod.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY amooora amooora

RUN pip install -e amooora

COPY pkl pkl
COPY raw_data raw_data

CMD uvicorn amooora.api.fast:app --host 0.0.0.0 --port $PORT
