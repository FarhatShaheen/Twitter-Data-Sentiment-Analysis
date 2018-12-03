''' main.py
    Do NOT modify this file!
'''
from hwcode import *

def main():
    # Exercise 1 : Part 1
    print("EXERCISE 1:")
    total_users = total_number_of_users('./data/data.jsonl')
    try:
        assert(type(total_users) is int)
    except:
        print("ERROR: total_number_of_users should return an int")

    print("The dataset has {} users".format(total_users))

    total_tweets = total_number_of_tweets('./data/data.jsonl')
    try:
        assert(type(total_tweets) is int)
    except:
        print("ERROR: total_number_of_tweets should return an int")
    print("The dataset has {} tweets".format(total_tweets))

    # Exercise 1 : Part 2

    avg_tweets_p_user = average_tweets_per_user('./data/data.jsonl')
    try:
        assert(type(avg_tweets_p_user) is float)
    except:
        print("ERROR: average_tweets_per_user should return a float")
    print("The dataset has an average of {0:.2f} tweets per user".format(avg_tweets_p_user))

    max_tweets_p_user = max_tweets_per_user('./data/data.jsonl')
    try:
        assert(type(max_tweets_p_user) is int)
    except:
        print("ERROR: max_tweets_per_user should return an int")
    print("The user with the most tweets has {} tweets".format(max_tweets_p_user))

    # Exercise 1 : Part 3

    most_tweets_user = user_with_most_tweets('./data/data.jsonl')
    try:
        assert(type(most_tweets_user) is str)
    except:
        print("ERROR: user_with_most_tweets should return a string")
    print("The user with the most tweets is {}".format(most_tweets_user))
    print()

    # Exercise 2 : Part 1
    print("EXERCISE 2:")
    positive_words = set()
    negative_words = set()
    with open('./data/bing_liu/negative-words.txt', encoding="cp1252") as in_file:
        for row in in_file:
            negative_words.add(row.strip())
    with open('./data/bing_liu/positive-words.txt', encoding="cp1252") as in_file:
        for row in in_file:
            positive_words.add(row.strip())

    predictions = classify_tweets('./data/data.jsonl', positive_words, negative_words) 
    try:
        assert(type(predictions) is list)
    except:
        print("ERROR: classify_tweets should return a list")
    print("Number of predicted positive tweets: {}".format(predictions.count("positive")))
    print("Number of predicted negative tweets: {}".format(predictions.count("negative")))
    print("Number of predicted neutral tweets: {}".format(predictions.count("neutral")))

    # Exercise 2 : Part 2
    negative_tweet = most_negative_tweet('./data/data.jsonl', positive_words, negative_words) 
    try:
        assert(type(negative_tweet) is str)
    except:
        print("ERROR: most_negative_tweet should return a string")
    print("The most negative tweet: {}".format(negative_tweet))

    positive_tweet = most_positive_tweet('./data/data.jsonl', positive_words, negative_words) 
    try:
        assert(type(positive_tweet) is str)
    except:
        print("ERROR: most_positive_tweet should return an string")
    print("The most positive tweet: {}".format(positive_tweet))
    print()

    one_neg_users = most_negative_users('./data/data.jsonl', positive_words, negative_words, 1)
    try:
        assert(type(one_neg_users) is list)
    except:
        print("ERROR: most_negative_users should return a list")

    try:
        assert(len(one_neg_users) == 10)
    except:
        print("ERROR: most_negative_users should return a list of length 10")

    print("The most negative users that tweeted at least once:")
    for i,screen_name in enumerate(one_neg_users):
        print("{0}: {1}".format(i,screen_name))
    print()

    five_neg_users = most_negative_users('./data/data.jsonl', positive_words, negative_words, 5)
    try:
        assert(type(five_neg_users) is list)
    except:
        print("ERROR: most_negative_users should return a list")

    try:
        assert(len(five_neg_users) == 10)
    except:
        print("ERROR: most_negative_users should return a list of length 10")
    print("The most negative users that tweeted at least five times:")
    for i,screen_name in enumerate(five_neg_users):
        print("{0}: {1}".format(i,screen_name))
    print()

    one_pos_users = most_positive_users('./data/data.jsonl', positive_words, negative_words, 1)
    try:
        assert(type(one_pos_users) is list)
    except:
        print("ERROR: most_positive_users should return a list")

    try:
        assert(len(one_pos_users) == 10)
    except:
        print("ERROR: most_positive_users should return a list of length 10")

    print("The most positive users that tweeted at least once:")
    for i,screen_name in enumerate(one_neg_users):
        print("{0}: {1}".format(i,screen_name))
    print()

    five_pos_users = most_positive_users('./data/data.jsonl', positive_words, negative_words, 5)
    try:
        assert(type(five_pos_users) is list)
    except:
        print("ERROR: most_positive_users should return a list")
    try:
        assert(len(five_pos_users) == 10)
    except:
        print("ERROR: most_positive_users should return a list of length 10")
    print("The most positive users that tweeted at least five times:")
    for i,screen_name in enumerate(five_neg_users):
        print("{0}: {1}".format(i,screen_name))
    print()

    # Extra Credit
    print("EXTRA CREDIT")
    days_most = dates_with_most_tweets('./data/data.jsonl')
    try:
        assert(type(days_most) is list)
    except:
        print("ERROR: days_with_most_tweets should return a list")
    try:
        assert(len(days_most) == 3)
    except:
        print("ERROR: dates_with_most_tweets should return a list of length 10")
    print("The dates with the most tweets:")
    for i,date in enumerate(days_most):
        print("{0}: {1}".format(i,date))

    print()
    days_least = dates_with_least_tweets('./data/data.jsonl')
    try:
        assert(type(days_least) is list)
    except:
        print("ERROR: days_with_least_tweets should return a list")
    try:
        assert(len(days_least) == 3)
    except:
        print("ERROR: dates_with_least_tweets should return a list of length 10")
    print("The dates with the least number of tweets:")
    for i, date in enumerate(days_least):
        print("{0}: {1}".format(i, date))



if __name__ == '__main__':
    main()
