FROM python:3.8-slim
ARG start_int=1000
ARG stop_int=2000
ENV START_INT=$start_int
ENV STOP_INT=$stop_int
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /prim

COPY api-primecalc.py /prim

COPY requirements.txt /prim/ 
RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "api-primecalc:app", "--reload", "--host", "0.0.0.0"]
