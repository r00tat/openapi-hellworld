FROM python:3

WORKDIR /app
RUN pip install connexion connexion[swagger-ui] swagger-ui-bundle
COPY *.py /app
COPY openapi/ /app/openapi/

CMD ["python3", "hello.py"]
EXPOSE 9001
