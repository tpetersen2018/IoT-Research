FROM ubuntu:20.04
# ADD RPi.GPIO-0.7.0 RPi.GPIO-0.7.0
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install smbus2

# Copy files
WORKDIR /server
COPY ./src/. /server
RUN chmod 755 /server/start.sh

# Expose port and run
EXPOSE 31337
CMD ["./start.sh"]
