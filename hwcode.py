import json


def total_number_of_users(jsonl_filename):
    '''
    Returns the total number of tweets in jsonl_filename
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The total number (int) of tweets
    '''
    # Write code for exercise 1 part 1 here
    #!cat ../data/jsonl_filename
    my_json_file = open(jsonl_filename, encoding = 'utf8')
    total = 0
    unique = set()
    for line in my_json_file:
        data = json.loads(line.strip())
        user = data['user']['screen_name']
        unique.add(user)
    total = len(unique)
    my_json_file.close()
    return total

def total_number_of_tweets(jsonl_filename):
    '''
    Returns the total number of tweets in jsonl_filename
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The total number (int) of tweets
    '''
    # Write code for exercise 1 part 1 here
    with open(jsonl_filename, encoding = 'utf8') as data:
        total_t = 0
        for line in data:
            lines = json.loads(line.strip())
            lines = lines['full_text']
            total_t += 1
    return total_t

def average_tweets_per_user(jsonl_filename):
    '''
    Returns the average number of tweets per user
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The average number (float) of tweets tweeted by a user
    '''
    # Write code for exercise 1 part 2 here
    with open(jsonl_filename, encoding = 'utf8') as data:
        average = 0.0
        total = 0
        unique = set()
        for line in data:
            lines = json.loads(line.strip())
            user = lines['user']['screen_name']
            unique.add(user)
            lines = lines['full_text']
            total += 1
    unique_l = len(unique)
    average = total/unique_l
    return average

def max_tweets_per_user(jsonl_filename):
    '''
    Returns the max number of tweets made by a user
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The max number (int) of tweets tweeted by a user
    '''
    # Write code for exercise 1 part 2 here
    max_tweets = 0
    twitr = {}
    with open(jsonl_filename, encoding = 'utf8') as data:
        for line in data:
            lines = json.loads(line.strip())
            if lines['user']['screen_name'] in twitr:
                twitr[lines['user']['screen_name']] += 1
            else:
                twitr[lines['user']['screen_name']] = 1
    max_tweets = max(twitr.values())
    return max_tweets

def user_with_most_tweets(jsonl_filename):
    '''
    Returns the user who made the most tweets
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The screen_name (a string) of the user with the most tweets
    '''
    # Wrte code for exercise 1 part 3 here
    user_tweetsalot = ''
    twitr_u = {}
    with open(jsonl_filename, encoding = 'utf8') as data:
        for line in data:
            lines = json.loads(line.strip())
            if lines['user']['screen_name'] in twitr_u:
                twitr_u[lines['user']['screen_name']] += 1
            else:
                twitr_u[lines['user']['screen_name']] = 1
    user_tweetsalot = max(twitr_u.items(), key=lambda x: x[1])[0]
    return user_tweetsalot

def classify_tweets(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Classifies each tweet in jsonl_filename as either having positive
    or negative sentiment.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: A list of predictions (a list of strings "positive"
             or "negative") with a prediction for each tweet
    '''
    # Write code for exercise 2 part 1 here
    predictions = []
    with open(jsonl_filename, encoding = 'utf8') as data:

        for line in data:
            lines = json.loads(line.strip())
            lines = lines['full_text'].split()
            lines = [element.lower() for element in lines]
            P = 0
            N = 0
            for word in lines:
                if word in positive_lexicon:
                    P += 1
                elif word in negative_lexicon:
                    N += 1
                else:
                    continue
            if P > N:
                predictions.append('positive')
            elif P < N:
                predictions.append('negative')
            else:
                predictions.append('neutral')
    return predictions

def most_negative_tweet(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Return the tweet that is the "most" negative - has the most negative words.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: The most negatives tweet text (string) 
    '''
    
    most_negative_tweet = ''
    most_neg = {}
    with open(jsonl_filename, encoding = 'utf8') as data:
        for line in data:
            lines = json.loads(line.strip())
            lines = lines['full_text'].split()
            lines = [element.lower() for element in lines]
            N = 0
            for word in lines:
                if word in negative_lexicon:
                    N += 1
            most_neg[' '.join(lines)] = N
    most_negative_tweet = max(most_neg.items(), key=lambda x: x[1])[0]
    return most_negative_tweet
 
def most_positive_tweet(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Return the tweet that is the "most" positive - has the most positive words.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: The most negatives tweet text (string) 
    '''
    # Write code for the exercise 2 part 2 here.
    most_positive_tweet = ''
    most_pos = {}
    with open(jsonl_filename, encoding = 'utf8') as data:
        for line in data:
            lines = json.loads(line.strip())
            lines = lines['full_text'].split()
            lines = [element.lower() for element in lines]
            P = 0
            for word in lines:
                if word in positive_lexicon:
                    P += 1
            most_pos[' '.join(lines)] = P
    most_positive_tweet = max(most_pos.items(), key=lambda x: x[1])[0]
    return most_positive_tweet
 
def most_negative_users(jsonl_filename, positive_lexicon, negative_lexicon, min_tweets):
    '''
    Return the 10 most negative users in the jsonl_filename dataset.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :param int min_tweets: The minimum number of tweets a user must have
                           to be considered the most positive.
    :return: A list of the 10 most negative users (screen names /strings)
             in the dataset.
    '''
    # Write code for the exercise 2 part 3 here.
    most_negative_users = [] 
    negatives_per_user = {}
    tweets_per_user = {}
   
    with open(jsonl_filename, encoding = 'utf8') as data:
        for line in data:
            lines = json.loads(line.strip())
            tt = lines['full_text'].lower().split()
            tu = lines['user']['screen_name']
            P = 0
            N = 0
            for word in tt:
                if word in positive_lexicon:
                    P += 1
                elif word in negative_lexicon:
                    N += 1
                else:
                    continue
            if N > P:
                if tu in negatives_per_user:
                    negatives_per_user[tu] += 1
                else:
                    negatives_per_user[tu] = 1
            if tu in tweets_per_user:
                tweets_per_user[tu] += 1
            else:
                tweets_per_user[tu] = 1
    average_per_user = {}    
    for key,value in tweets_per_user.items():
        if value >= min_tweets:
            if key in negatives_per_user.keys():
                average_per_user[key] = negatives_per_user[key]/value 
    average_per_user = sorted(average_per_user, key=average_per_user.get, reverse=True)
    for i in range(10):
        most_negative_users.append(average_per_user[i])
    return most_negative_users


def most_positive_users(jsonl_filename, positive_lexicon, negative_lexicon, min_tweets):
    '''
    Return the 10 most positive users in the jsonl_filename dataset.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :param int min_tweets: The minimum number of tweets a user must have
                           to be considered the most positive.
    :return: A list of the 10 most positive users (screen names /strings)
             in the dataset.
    '''
    # Write code for the exercise 2 part 3 here.
    most_positive_users = [] 
    positives_per_user = {}
    tweets_per_userp = {}
   
    with open(jsonl_filename, encoding = 'utf8') as data:
        for line in data:
            lines = json.loads(line.strip())
            tt = lines['full_text'].lower().split()
            tu = lines['user']['screen_name']
            P = 0
            N = 0
            for word in tt:
                if word in positive_lexicon:
                    P += 1
                elif word in negative_lexicon:
                    N += 1
                else:
                    continue
            if P > N:
                if tu in positives_per_user:
                    positives_per_user[tu] += 1
                else:
                    positives_per_user[tu] = 1
            if tu in tweets_per_userp:
                tweets_per_userp[tu] += 1
            else:
                tweets_per_userp[tu] = 1
    average_per_userp = {}    
    for key,value in tweets_per_userp.items():
        if value >= min_tweets:
            if key in positives_per_user.keys():
                average_per_userp[key] = positives_per_user[key]/value 
    average_per_userp = sorted(average_per_userp, key=average_per_userp.get, reverse=True)
    for i in range(10):
        most_positive_users.append(average_per_userp[i])
    return most_positive_users

def dates_with_most_tweets(jsonl_filename):
    '''
    Returns a list of dates that had the most tweets.

    :param str jsonl_filename: The file path of the twitter dataset
    :return: A list of the 3 days (strings) with the most tweets
    '''
    # Write code for extra credit
    from datetime import datetime 
    days_with_most_tweets = []
    days = {}
    with open(jsonl_filename, encoding = 'utf8') as data:
        for line in data:
            lines = json.loads(line.strip())
            date = datetime.strptime(lines["created_at"], '%a %b %d %H:%M:%S %z %Y').strftime('%b %d %Y')
            if date in days:
                days[date] += 1
            else:
                days[date] = 1
    days = sorted(days, key=days.get, reverse=True)
    for i in range (3):
        days_with_most_tweets.append(days[i])
    return days_with_most_tweets 

def dates_with_least_tweets(jsonl_filename):
    '''
    Returns a list of dates that had the least tweets.

    :param str jsonl_filename: The file path of the twitter dataset
    :return: A list of the 3 days (strings) with the least tweets
    '''
    # Write code for extra credit
    from datetime import datetime    
    days_with_least_tweets = []
    days = {}
    with open(jsonl_filename, encoding = 'utf8') as data:
        for line in data:
            lines = json.loads(line.strip())
            date = datetime.strptime(lines["created_at"], '%a %b %d %H:%M:%S %z %Y').strftime('%b %d %Y')
            if date in days:
                days[date] += 1
            else:
                days[date] = 1
    days = sorted(days, key=days.get)
    for i in range (3):
        days_with_least_tweets.append(days[i])
    return days_with_least_tweets 

