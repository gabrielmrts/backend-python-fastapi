FROM python:3.13
WORKDIR /var/www/app
ADD . .
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["/var/www/app/container.sh"]