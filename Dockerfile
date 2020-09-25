FROM python

WORKDIR /blog
COPY . /blog

RUN pip install -r requirements.txt
CMD python app.py
