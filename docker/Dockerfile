FROM python:3.12-rc-slim-buster

# install time zone
ENV TZ="Europe/Moscow"
RUN apt-get install -y tzdata
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install library
COPY requirements.txt .
RUN pip3 install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# copy all files to /app directory and move into directory.
COPY . /app
WORKDIR /app

CMD ["python", "main.py"]