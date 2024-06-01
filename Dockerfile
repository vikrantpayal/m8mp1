# pull python base image
FROM python:3.10-slim
# copy application files
ADD *.pkl .
ADD *.py .
ADD requirements.txt .
ADD *.whl .

# specify working directory
WORKDIR .
# update pip
RUN pip install --upgrade pip
# install dependencies
RUN pip install -r requirements.txt

RUN rm *.whl 

COPY app/. app/.

# expose port for application
EXPOSE 8080 
#8001

# start fastapi application
CMD ["python", "app.py"]