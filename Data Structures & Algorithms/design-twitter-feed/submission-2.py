import heapq

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posting = defaultdict(list)
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posting[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        
        users = self.following[userId] | {userId}

        for uid in users:
            if self.posting[uid]:
                idx = len(self.posting[uid]) - 1
                time, postId = self.posting[uid][idx]
                heapq.heappush(
                    heap,(-time,postId,uid,idx)
                )
        
        while heap and len(res) < 10:
            time, postId, uid, idx = heapq.heappop(heap)
            res.append(postId)
            
            if idx > 0:
                time, postId = self.posting[uid][idx-1]
                heapq.heappush(heap,(-time, postId, uid, idx-1))
                
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)