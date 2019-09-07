class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.subscriptions = {}
        self.timestep = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.tweets:
            self.tweets[userId] = []
            
        if userId not in self.subscriptions:
            self.subscriptions[userId] = set()
            self.subscriptions[userId].add(userId)
            
        self.tweets[userId].insert(0, (-self.timestep, tweetId))
        self.timestep += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feeds = []
        if userId not in self.subscriptions:
            return feeds
        
        for user in self.subscriptions[userId]:
            if user in self.tweets:
                for tweet in self.tweets[user][:10]:
                    feeds.append(tweet)
        
        heapq.heapify(feeds)
        max_num_tweet = min(10, len(feeds))
        count = 0
        res = []
        while count < max_num_tweet:
            res.append(heapq.heappop(feeds)[1])
            count += 1
            
        return res
        
        
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.subscriptions:
            self.subscriptions[followerId] = set()
            self.subscriptions[followerId].add(followerId)
        self.subscriptions[followerId].add(followeeId)
        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId and followerId in self.subscriptions and followeeId in self.subscriptions[followerId]:
            self.subscriptions[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)