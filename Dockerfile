
FROM python:3.8
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet'); nltk.download('stopwords')"
COPY . .
EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "nlpApp.py" ]