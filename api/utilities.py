import re 
import pickle 
from  nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords


# defining dictionary containing all emojis with their meaning, 
emojis = {
    ':)':'smile', ':-)':'smile',';d':'wink', ':-E':'vampire',':(':'sad',':-(':'sad', ':-<':'sad',':P':'raspberry',':O':'surprised',
    ':-@':'shocked',':@':'shocked',':-$':'confused',':\\':'annoyed', ':#':'mute', ':X':'mute', ':^)':'smile', ':-&':'confused','$_$':'greedy',
    '@@':'eyeroll',':-!':'confused',':-D':'smile',':-0':'yell','O.o':'confused',
    '<(-_-)>':'robot','d[-_-]b':'dj',":'-)":'sadsmile',';)':'wink',';-)':'wink','O:-)':'angel', 'O*-)':'angel','(:-D':'gossip', '=^.^=':'cat'}

lemmatizer = WordNetLemmatizer()
# grouping toghther the inflected form ('better.>good)
stopwords = set(stopwords.words('english'))
with open('models/pipeline.pickle', 'rb') as f:
    loaded_pipe = pickle.load(f)

def predict_pipeline(text):
    return predict(loaded_pipe, text)

def preprocess(textdata):
    processed_texts = []
    # Defining regex patterns 
    url_pattern = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    user_pattern = '@[^\s]+'
    alpha_pattern = "[^a-zA-Z0-9]"
    sequence_pattern = r"(.)\1\1+"
    seq_replace_pattern = r"\1\1"

    for tweet in textdata:
        tweet = tweet.lower()
        # replace all urls with 'url'
        tweet = re.sub(url_pattern, 'URL', tweet)
        # Replace all emojis 
        for emoji in emojis.keys():
            tweet = tweet.replace(emoji, 'EMOJI'+emojis[emoji])
        # replace @username to user 
        tweet = re.sub(user_pattern, 'USER', tweet)
        # replace all non alphabets
        tweet = re.sub(alpha_pattern, " ", tweet)
        # replace 3 or more consecutive letters by 2 letter. 
        tweet = re.sub(sequence_pattern, seq_replace_pattern,tweet)

        preprocessed_words = []
        for word in tweet.split():
            if len(word)>1 and word not in stopwords:
                # lemmatize the word 
                word = lemmatizer.lemmatize(word)
                preprocessed_words.append(word)
        processed_texts.append(' '.join(preprocessed_words))
    return processed_texts


def predict(model, text):
    # predict the sentiment
    preprocessed_text = preprocess(text)
    predictions = model.predict(preprocessed_text)
    pred_to_label = {0:'Negative', 1:'Positive'}
    # Make a list of text with sentimet 
    data = []
    for t, pred in zip(text, predictions):
        data.append({'text':t,'pred': int(pred),'label': pred_to_label[pred]})
    return data 
# if __name__ == "__main__":
#     # Text to classify shold be in a list 
#     text = ["I hate something", 
#            "May the force bad bad bad.",
#            "Mr. stark, I don't feel so good. "]
#     predictions = predict_pipeline(text)
#     print(predictions)