FROM python:3

ENV DISCORD_TOKEN "<discord token>"

COPY requirements.txt .
COPY *.py .

RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python", "main.py" ]

