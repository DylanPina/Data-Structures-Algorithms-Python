from collections import defaultdict
from heapq import nlargest
from typing import List


class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweetCount = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweetCount, tweetId))
        self.tweetCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for followee in self.following[userId] | {userId}:
            feed.extend(self.tweets[followee])
        return [tweetId for _, tweetId in nlargest(10, feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
