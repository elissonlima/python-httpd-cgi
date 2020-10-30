# Python HTTPD CGI Image

This is a docker image for learning purposes. I create a user docker image based on httpd:2.4 official image. Then I modified the httpd.conf file for cgi support and delivered a test-cgi.py that is back preprocessed and out the web page

## Use

- Run `docker build -t python-httpd-cgi .` inside the main directory
- Run `docker run --rm -it -p 8080:80 python-httpd-cgi`
- Acess localhost:8080/cgi/test-cgi.py for the a test page or put your own python script inside the python-cgi folder before build and acess with localhost:8080/cgi/<your_python_script.py>