from collections import defaultdict
class Twitter:

    def __init__(self):
        self.idx = 0
        self.tweetmap = defaultdict(list)
        self.followeemap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followeemap[userId].add(userId)
        self.tweetmap[userId].append((self.idx, tweetId))
        self.idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        for followee in self.followeemap[userId]:
            tweets = self.tweetmap[followee]
            if len(tweets) > 0:
                last = len(tweets) - 1
                print(last)
                idx, tweetID = tweets[last]
                heapq.heappush(maxHeap, (-idx, tweetID, followee, last))
        
        while maxHeap and len(res) < 10:
            if maxHeap:
                neg_idx, tweetID, followee, last = heapq.heappop(maxHeap)
                res.append(tweetID)
                if last > 0:
                    lastidx, last_tweet_id = self.tweetmap[followee][last - 1]
                    heapq.heappush(maxHeap,(-lastidx,last_tweet_id, followee, last - 1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followeemap[followerId]:
            self.followeemap[followerId].add(followerId)
        self.followeemap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeemap[followerId]:
            self.followeemap[followerId].discard(followeeId)
