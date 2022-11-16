FROM python:3.10

WORKDIR /usr/app/src

# RUN pip3 install requests
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD main.py ./

ENTRYPOINT ["python", "./main.py"]
# CMD ["python", "./main.py", "(SEARCH)"]