import json
import sys
from typing import *
import nltk


def main():
    negative_tweets = read_tweets(sys.argv[1], "negative")
    positive_tweets = read_tweets(sys.argv[2], "positive")
    full_set = strip_tweets(negative_tweets, positive_tweets)
    get_tweet_words(full_set)
    word_list = get_tweet_words(full_set)
    featured_words = get_amount_words(word_list)
    # print(extract_features(negative_tweets[0],featured_words))


def read_tweets(filename1: str, sentiment: str) -> List[Tuple[str, str]]:
    """
    Function which reads a json file and returns a List of tuples with a tweet and sentiment.
    :param filename1: Negative tweets (dataset)
    :param sentiment: Postive tweets (dataset)
    :return: List of tuples containing a tweet and sentiment
    """
    tweets = []
    with open(filename1, 'r') as json_file:
        for line in json_file:
            tweet = (json.loads(line))
            tweet_tuple = (tweet["text"], sentiment)
            tweets.append(tweet_tuple)
    return tweets


def strip_tweets(negative_tweets: List[Tuple[str, str]], positive_tweets: List[Tuple[str, str]])->List[Tuple[str, str]]:
    """
    Function which strips small words that shouldn't be considered from the data set
    and combines negative and positive tweets.
    :param negative_tweets: Negative set
    :param positive_tweets: Postive set
    :return: Full dataset combined
    """
    tweets = []
    for (words, sentiment) in negative_tweets + positive_tweets:
        filtered_users_tags = [word.lower() for word in words.split() if len(word) >= 3 and '@' != word[0][:1] and '#' != word[0][:1] and '&' != word[0][:1] and 'http' != word]
        filtered_links = [word for word in filtered_users_tags if 'http' not in word]
        filtered_punct = [word.strip(".,?!") for word in filtered_links]
        filtered = [word.replace('...', ' ') for word in filtered_punct]
        print(filtered)
        # tweets.append((filtered, sentiment))
    return tweets


def get_tweet_words(tweet_set: List[Tuple[str, str]])->List[str]:
    """
    function that gets all words from a tweet set
    :param tweet_set:
    :return: List of words
    """
    words_list = []
    for(words, sentiment) in tweet_set:
        words_list.extend(words)
    return words_list


def get_amount_words(wordlist: List[str])->KeysView:
    """
    Function that counts the amount of occurrences in a word list and returns the dict with the amount
    :param wordlist: The wordlist
    :return: Dictionary with the word and amount it occurred in the set
    """
    word_list = nltk.FreqDist(wordlist)
    featured_words = word_list.keys()
    return featured_words


def extract_features(document, featured_words):
    document_words = set(document)
    features = {}
    for word in featured_words:
        features['contains(%s)' % word] = (word in document_words)
    return features


if __name__ == '__main__':
    main()
