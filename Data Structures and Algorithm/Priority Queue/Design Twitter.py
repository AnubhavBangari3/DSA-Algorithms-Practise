import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        # Decreasing timestamp:
        # newer tweets have smaller values such as 0, -1, -2...
        # This allows Python's Min Heap to return the newest tweet first.
        self.time = 0

        # follower_id -> set of followee IDs
        self.following = defaultdict(set)

        # user_id -> list of [timestamp, tweet_id]
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store the tweet in posting order.
        self.tweets[userId].append([self.time, tweetId])

        # Decrease time so every newer tweet gets a smaller timestamp.
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Include the user's own tweets in their feed.
        users = self.following[userId] | {userId}

        # Heap entry:
        # [timestamp, tweet_id, user_id, tweet_index]
        min_heap = []

        # Add only the latest tweet of every relevant user.
        for followee_id in users:
            last_index = len(self.tweets[followee_id]) - 1

            if last_index >= 0:
                timestamp, tweet_id = self.tweets[followee_id][last_index]

                heapq.heappush(
                    min_heap,
                    [timestamp, tweet_id, followee_id, last_index]
                )

        news_feed = []

        # Repeatedly take the newest available tweet.
        while min_heap and len(news_feed) < 10:
            timestamp, tweet_id, followee_id, index = heapq.heappop(min_heap)

            news_feed.append(tweet_id)

            # After taking this user's latest tweet,
            # add their next older tweet to the heap.
            if index > 0:
                previous_timestamp, previous_tweet_id = (
                    self.tweets[followee_id][index - 1]
                )

                heapq.heappush(
                    min_heap,
                    [
                        previous_timestamp,
                        previous_tweet_id,
                        followee_id,
                        index - 1
                    ]
                )

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # A set automatically prevents duplicate follow relationships.
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard() safely removes the followee even if not present.
        self.following[followerId].discard(followeeId)

'''
Algorithm

1. Maintain a global decreasing timestamp.

2. For every user, store their tweets as:

   [timestamp, tweet_id]

3. For every follower, maintain a set
   of users they follow.

4. To post a tweet:

   a. Append the timestamp and tweet ID
      to the user's tweet list.

   b. Decrease the timestamp.

5. To generate a news feed:

   a. Consider:
      - The user themself
      - Every user they follow

   b. Insert the latest tweet of each relevant user
      into a Min Heap.

   c. Remove the newest tweet from the heap.

   d. Add its tweet ID to the result.

   e. Insert the next older tweet
      from the same user into the heap.

   f. Repeat until:
      - 10 tweets are collected, or
      - The heap becomes empty.

6. To follow:
   - Add the followee to the follower's set.

7. To unfollow:
   - Remove the followee from the follower's set.

Pattern:
Heap + Hash Map + Set + K-Way Merge

Time Complexity:

postTweet():
O(1)

follow():
O(1) average

unfollow():
O(1) average

getNewsFeed():
O(F + 10 log F)

Space Complexity:
O(T + R)

Where:

F = number of followed users
T = total tweets
R = total follow relationships

'''