FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install smbus2 Flask python-dotenv

# Copy files
WORKDIR /server
COPY ./src/. /server
RUN chmod 755 /server/start.sh

# Expose port and run
EXPOSE 80
CMD ["./start.sh"]
