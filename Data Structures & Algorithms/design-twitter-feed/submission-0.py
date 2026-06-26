import heapq
from typing import List

class Twitter:

    def __init__(self):
        # CHANGED: need to store on self
        self.follow_list = {}
        self.tweets_by_user = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # CHANGED: use [] instead of (), use self.time, and handle append correctly
        if userId not in self.tweets_by_user:
            self.tweets_by_user[userId] = []
        self.tweets_by_user[userId].append([self.time, tweetId])

        # CHANGED: init follow_list and make user follow themselves
        if userId not in self.follow_list:
            self.follow_list[userId] = set()
        self.follow_list[userId].add(userId)

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        k = 10  # CHANGED: define k

        # CHANGED: handle user not in follow_list
        if userId not in self.follow_list:
            return []

        # CHANGED: use self. and [] instead of ()
        for user in self.follow_list[userId]:
            for tweet in self.tweets_by_user.get(user, []):
                heapq.heappush(maxheap, tweet)
                if len(maxheap) > k:
                    heapq.heappop(maxheap)

        # Now maxheap has up to k most recent tweets (by negative time)
        res = []
        while maxheap:
            res.append(heapq.heappop(maxheap)[1])
        # heap pops oldest of the kept ones last, so reverse to get most recent first
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        # CHANGED: use self.[], sets, and correct variable name
        if followerId not in self.follow_list:
            self.follow_list[followerId] = set()
        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # CHANGED: use self.[], and correct variable name
        if followerId in self.follow_list and followeeId in self.follow_list[followerId]:
            # optional: don't allow unfollow self
            if followeeId != followerId:
                self.follow_list[followerId].remove(followeeId)

