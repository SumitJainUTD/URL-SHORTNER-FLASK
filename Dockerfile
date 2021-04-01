FROM python:3.6-stretch

#RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

WORKDIR /url_shortener

COPY . /url_shortener

RUN pip --no-cache-dir install -r url_shortener/requirements.txt

EXPOSE 4000

ENTRYPOINT ["python3"]
CMD ["main.py"]