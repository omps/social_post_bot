"""Module to add hashtags to the post message."""

import random

def add_hashtags(post_message, hashtags, sm_account):
    """Add hashtags to the post message if space permits."""
    # Make the string into a list
    hashtags = hashtags.split(",")
    hashtag_count = 0
    probabilities = [0, 1, 2, 3]
    rm_hashtag_prob = random.choice(probabilities)
    print(f"Number that triggers additional hashtags = 1, your number = {rm_hashtag_prob}")
    if rm_hashtag_prob == 1:
        hashtags.insert(0, "RocketMovingApp")
        print(f"Adding 'RocketMovingApp' to hashtags")
    else:
        pass

    # For Twitter
    if sm_account == "tw":
        for hashtag in hashtags:
            hashtag = hashtag.strip()
            hashtag = " #"+hashtag
            # If length permits, add a hashtag
            if len(post_message+" "+hashtag) < 280:
                post_message = post_message+" "+hashtag
                print(f"Added hashtag '{hashtag}' to the post message.")
            # Otherwise, don't add a hashtag
            else:
                post_message = post_message
                break

    # For all other social media platforms
    elif sm_account != "tw":        
        hashtag_count = 0
        for hashtag in hashtags:
            hashtag = hashtag.strip()
            hashtag = " #"+hashtag
            # If length permits, add a hashtag
            if len(post_message+"\n"+hashtag) < 2000 and hashtag_count < 10:
                post_message = post_message+" "+hashtag
                hashtag_count += 1
                print(f"Added hashtag '{hashtag}' to the post message.")
            # Otherwise, don't add a hashtag
            else:
                post_message = post_message
                hashtag_count += 1
                break

    return post_message