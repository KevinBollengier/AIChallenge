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

#### Why analyse tweets?

Originally I wanted to use this method to categorize Jihadi tweets, due to lack of a good dataset, I chose to extend the
the problem to something more general. Nowadays "social-media" is a great source of big data. The possibilities are endless.
Marketing departments can use tweets to check how people feel about a newly released product to quickly adapt their marketing
strategies. 

For example: Star Wars Battlefront II was released on november 17 and received a lot of backlash due to the
pay to win in the game. If they use the Twitter API they can quickly get a view on how many users are tweeting negative things about the game.

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

As you can see, the tweet that this algorithm never saw classified it as a negative tweet. This could be used to get automated feedback
about new products. 

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

But we could even go further, because social media can also be used as indicator to find if people are coping with depression
or even suicidal thoughts.

```
Enter another tweet to classify or type exit to quit
I feel so depressed.. I just want to die right now...
negative

```

Social media could use this to help with suicide prevention.

### Why did I chose this subject?

Well basically social media, are not social media anymore. They are one of the best examples of "open (big) data". This data is used everywhere and most of it is publicly reachable for anyone.

Intelligence agencies use this stuff to search for criminals, terrorism suspects, ...
Marketeers use it for building marketing strategies.

In my opinion it could be a nice use to monitor cyber bullying and classifying people with mental problems.

### Why use Artificial Intelligence for this?

Well, with social media, we are working with massive datasets, which is just too much to manually handle. Also an AI thinks rationally compared to a human doing this job.
We might consider a negative positive, or the other way around based on how we feel on that same moment. As example of the Star Wars tweet, you might consider it positive, because you don't like Star Wars or EA in general.

### Existing examples of social media analysis using Artificial Intelligence

- In the events of the Snowden leaks, it was confirmed that the NSA was using social media to spy on people and categorize them as potential threat or not.
- Companies are already using social media to improve the customer experience by analysing what people are tweeting about them.


### Analysis

I am using a test set of 400 lines of twitter data and the accuracy of the algorithm is 83.5%

This is done by classifying the data (without the labels) and then compare them to the label they were given.

```
Training the algorithm, please wait, this can take a while!
Algorithm trained, please wait calculating accuracy...
Classifier accuracy percentage:  83.5

```
