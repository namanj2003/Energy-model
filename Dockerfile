FROM python:3.8-slim

WORKDIR /opt/ml

COPY model.tar.gz /opt/ml/model.tar.gz
COPY wheels/ /opt/ml/wheels/
COPY inference.py /opt/ml/inference.py

RUN pip install --no-index --find-links=/opt/ml/wheels flask numpy pandas scikit-learn

EXPOSE 8080
CMD ["python", "/opt/ml/inference.py"]
