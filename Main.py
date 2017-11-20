import json
import sys
from typing import *
import nltk


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


negative_tweets = read_tweets(sys.argv[1], "negative")
positive_tweets = read_tweets(sys.argv[2], "positive")

CONST_NEG_TEST = read_tweets("Datasets/negative_test.json", "negative")
COnSt_POS_TEST = read_tweets("Datasets/positive_test.json", "positive")


def strip_tweets(negative_tweets: List[Tuple[str, str]], positive_tweets: List[Tuple[str, str]]) -> List[
    Tuple[str, str]]:
    """
    Function which strips small words that shouldn't be considered from the data set
    and combines negative and positive tweets.
    :param negative_tweets: Negative set
    :param positive_tweets: Postive set
    :return: Full dataset combined
    """
    tweets = []
    for (words, sentiment) in negative_tweets + positive_tweets:
        filtered_users_tags = [word.lower() for word in words.split() if
                               len(word) >= 3 and
                               '@' != word[0][:1] and
                               '#' != word[0][:1] and
                               '&' != word[0][:1] and
                               'http' != word]
        filtered_links = [word for word in filtered_users_tags if 'http' not in word]
        filtered_punct = [word.strip(".,?!") for word in filtered_links]
        filtered = [word.replace('...', ' ') for word in filtered_punct]
        tweets.append((filtered, sentiment))
    return tweets


tweets = strip_tweets(negative_tweets, positive_tweets)
test_tweets = strip_tweets(CONST_NEG_TEST, COnSt_POS_TEST)


def get_tweet_words(tweet_set: List[Tuple[str, str]]) -> List[str]:
    """
    function that gets all words from a tweet set
    :param tweet_set:
    :return: List of words
    """
    words_list = []
    for (words, sentiment) in tweet_set:
        words_list.extend(words)
    return words_list


def get_word_features(wordlist: List[str]) -> KeysView:
    """
    Function that counts the amount of occurrences in a word list and returns the dict with the amount
    :param wordlist: The wordlist
    :return: Dictionary with the word and amount it occurred in the set
    """
    word_list = nltk.FreqDist(wordlist)
    featured_words = word_list.keys()
    return featured_words


word_features = get_word_features(get_tweet_words(tweets))


def extract_features(tweet: List[str]) -> Dict:
    """
    Function that returns dict of words with true and false depending if the tweet contains the word or not
    :param tweet: A string of text or "tweet" which is going to be classified, it's a list because we need to consider
    every word individually
    :return: Dict of words with true/false labels depending if the word is inside the tweet or not
    """
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)
    return features


training_set = nltk.classify.util.apply_features(extract_features, tweets)
test_set = nltk.classify.util.apply_features(extract_features, test_tweets)


def main():
    print("Training the algorithm, please wait, this can take a while!")
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("Algorithm trained, please wait calculating accuracy...")
    print("Classifier accuracy percentage: ", (nltk.classify.accuracy(classifier, test_set)) * 100)
    tweet = input("Enter your tweet to classify: \n")
    print(classifier.classify(extract_features(tweet.split())))
    while tweet != "exit":
        tweet = input("Enter another tweet to classify or type exit to quit\n")
        if tweet != "exit":
            print(classifier.classify(extract_features(tweet.split())))


if __name__ == '__main__':
    main()
