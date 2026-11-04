
from limiters.token_bucket import TokenBucketRateLimiter
import time

def test_buckect_first_request_allowed():
    rate_limiter = TokenBucketRateLimiter(5,3)
    assert rate_limiter.allow_requests() == False
    # wait for 1 second to refill the bucket
    
    time.sleep(1)
    assert rate_limiter.allow_requests() == True