FROM mcr.microsoft.com/playwright/python:v1.53.0-jammy


RUN apt-get update && \
    apt-get install -y curl unzip openjdk-11-jre && \
    curl -o allure.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure.tgz


WORKDIR /usr/workspace


COPY ./requirements.txt .


RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .
