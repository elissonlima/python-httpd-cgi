FROM httpd:2.4

COPY ./public-html /usr/local/apache2/htdocs/

RUN apt-get update && apt-get install -y python3

RUN mkdir /usr/local/my-site

COPY ./python-cgi /usr/local/my-site

RUN chown -R www-data:www-data /usr/local/my-site

RUN chmod +x /usr/local/my-site/*

COPY ./cfg/my-httpd.conf /usr/local/apache2/conf/httpd.conf
