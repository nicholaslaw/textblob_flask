FROM python:3.6.5-jessie

COPY requirements.txt /
RUN pip install -r /requirements.txt
CMD ["python", "app.py"]