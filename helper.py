from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


def split_into_lemmas(message):
    message = message.lower()
    words = TextBlob(message).words
    # for each word, take its "base form" = lemma 
    return [word.lemma for word in words]


class TfidfVectorizer():
    
    def __init__(self, data):
        self.bow = CountVectorizer(\
                        analyzer=split_into_lemmas)\
                    .fit(data)

        
    def tfidf_vector(self, data):
        bow_d = self.bow.transform(data)
        tfidf = TfidfTransformer().fit(bow_d)
        tfidf_d = tfidf.transform(bow_d)
        
        return tfidf_d
    
