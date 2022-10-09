FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv


COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["Q5.py","./"]

EXPOSE 9696

ENTRYPOINT [ "waitress-serve" ,"--listen=0.0.0.0:9696", "Q5:app"]
