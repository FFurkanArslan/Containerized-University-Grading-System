FROM python:latest
WORKDIR /home/quiblord/Desktop/FFlaskBlueprint
COPY . .
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3","run.py"];
