FROM python:3.7

ADD . .

RUN pip install --upgrade pip

CMD [ "python","-m", "uniittest", "discover", "-s", "Tests" ]
