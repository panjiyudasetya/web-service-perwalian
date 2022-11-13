FROM python:3.7

# Set working directory
WORKDIR /web-service-perwalian

# Add everything inside the `web-service-perwalian` local directory
# into the working directory
ADD . /web-service-perwalian/

# Install all requirements 
RUN pip install -r requirements.txt

# Run server of the web service app
RUN chmod +x ./runserver.sh
CMD ["sh", "runserver.sh"]
