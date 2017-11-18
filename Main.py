import json
import sys
from typing import *


def main():
    negative_tweets = read_tweets(sys.argv[1], "negative")
    positive_tweets = read_tweets(sys.argv[2], "positive")
    full_set = strip_tweets(negative_tweets, positive_tweets)
    get_tweet_words(full_set)
    word_list = get_tweet_words(full_set)
    print(word_list)


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
        filtered = [word.lower() for word in words.split() if len(word) >= 3]
        tweets.append((filtered, sentiment))
    # print(tweets)
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
    # print(words_list)
    return words_list


def get_amount_words():
    pass


if __name__ == '__main__':
    main()
