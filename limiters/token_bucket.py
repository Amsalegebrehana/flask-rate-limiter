from flask import Flask, jsonify, request
import datetime
import time

# let's say there is this bucket [] it's max size is 5
# the token per second is 3 tokens
# when a request 
## e.g 1 sec - the bucket is empty so can be filled with 3 tokens then 2 requests came 
# uses 2 of the existing tokens then continue
## 2 sec - the bucket has 1 token when 3 token added now it has 4 tokens. at this second a user made 5 requests 
# this uses all the 4 tokens plus 1 request left gets discarded
## 3 sec -   bucket is empty so add 3 token no user request
## 4 sec - bucket already have 3 token when trying to add 3 it will add only 2 -> (-1) 
# if the users make 5 request now all req get processed

# token bucket algorithm implementation
class TokenBucketRateLimiter:

    def __init__(self, max_capacity, refill_rate):
        self.max_capacity = max_capacity
        self.bucket_size = 0
        self.refill_rate = refill_rate #tokens per second
        self.last_refill_time = time.monotonic()

    def refill(self):

        current_second = time.monotonic()
        time_passed = current_second - self.last_refill_time
        if self.bucket_size < self.max_capacity:
            self.bucket_size += (self.refill_rate * time_passed)
            if self.bucket_size > self.max_capacity:
                self.bucket_size = self.max_capacity
        self.last_refill_time = current_second

    def allow_requests(self):

        if self.max_capacity <= 0:
            return False
        self.refill()
    
        if self.bucket_size >= 1:
            self.bucket_size -= 1
        else:
            return False

        return True
    
