FROM python:3.10.7-slim

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]