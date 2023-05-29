# take the python image
FROM python:3.11

# create a workfolder `app`
WORKDIR /app 

# doesn't matter if COPY or ADD (here!)
ADD requirements.txt /app
ADD get_reddits.py /app
ADD config.py /app

# install everything mentioned in the requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#run python script get_reddits.py
CMD ["python", "get_reddits.py"]
