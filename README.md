# AI Challenge
## Twitter sentiment analyser
### Documentation

Run the tool from the commandline with 2 arguments:
- The negative tweets in json format (Datasets/negative_set.json)
- The positive tweets in json format (Datasets/positive_set.json)

Example:
```
python Main.py Datasets/negative_tweets.json Datasets/positive_tweets.json
```

### Justification

#### Why did I choose this subject?

Because I believe that social media, are no longer social. They are one of the best examples of "open (big) data".
This data is used everywhere and most of it is publicly available for everyone.

Intelligence agencies use this data to search for criminals, terrorism suspects, ...
Marketeers use it for building marketing strategies.

Instead of using it for profitability, it could be used for something directly impacting the life of a human being,
namely monitoring cyber bullying and identifying people with mental issues.

#### Why analyse tweets?

Originally I wanted to use this method to categorize Jihadi tweets, but due to lack of a good dataset, I chose to extend the
the problem to something more general. Nowadays "social-media" is a wonderful source of big data. The possibilities are endless.
Marketing departments can use tweets to check how people feel about a newly released product to quickly adapt their marketing
strategies. 

For example: Star Wars Battlefront II was released on november 17 and received a lot of backlash due to the
pay to win strategy incorporated in the game mechanics. When using the Twitter API, the SWB II team can quickly obtain an overview of how many users are tweeting about their new product,
and can categorize them in positive and negative feelings toward their new game.

```
python Main.py Datasets/negative_tweets.json Datasets/positive_tweets.json
Training the algorithm, please wait, this can take a while!
Algorithm trained, please wait calculating accuracy...
Classifier accuracy percentage:  83.5
Enter your tweet to classify:
In case you didn't know, the backlash that EA got for the Star Wars Battlefront 2 microtransacti
on fiasco is having an effect industry wide. Been hearing from quite a few people lots of publis
hers are worried and have had meetings regarding what happened...
negative

```

As you can see, the tweet, which has never before been fed to the system, has been classified by this algorithm as a negative tweet.
This could be used to get automated feedback about new products.

What about the latest movie Thor Ragnarok?

```
Enter another tweet to classify or type exit to quit
Thor ragnarok is for sure the best movie of 2017! #ragnarok #marvel
positive

```

Or someone tweeting about "The avengers: Infinity War":

```
Enter another tweet to classify or type exit to quit
we should be ready because they can upload the infinity war trailer at anytime
positive

```

We could even go further: social media can also be used as indicator to find if people are coping with depression or even suicidal thoughts.

```
Enter another tweet to classify or type exit to quit
I feel so depressed.. I just want to die right now...
negative

```

Social media could use this to help with suicide prevention.


### Why use Artificial Intelligence for this?

The objectivity of AI and its innate ability to process large amounts of data in a relatively short amount of time makes it the best tool for this job.
Also a human may be biased by his own preference on a certain point of view, where a machine will not. e.g. Star wars tweet, may be considered positive by some who don't like Star wars or EA in general.

### Existing examples of social media analysis using Artificial Intelligence

- In the events of the Snowden leaks, it was confirmed that the NSA was using social media to spy on people and categorize them as potential threats.
- Companies are already using social media to improve the customer experience by analysing what people are tweeting about them.


### Analysis

I am using a test set of 400 lines of twitter data and the accuracy of the algorithm is 83.5%

This is done by classifying the data (without the labels) and then compare them to the label they were given in the test set.

```
Training the algorithm, please wait, this can take a while!
Algorithm trained, please wait calculating accuracy...
Classifier accuracy percentage:  83.5

```

As requested during the presentation I did the same with the training set:

```
Training the algorithm, please wait, this can take a while!
Algorithm trained, please wait calculating accuracy...
Classifier accuracy percentage:  93.15625
```

