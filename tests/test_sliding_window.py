from limiters.sliding_window import SlidingWindowRateLimiter

def test_first_request_allowed():
    rate_limiter = SlidingWindowRateLimiter(5,60)
    assert rate_limiter.allow_requests("client_1",10) == True

def test_request_limit_exceeded():
    rate_limiter = SlidingWindowRateLimiter(5,60)
    assert rate_limiter.allow_requests("client_1",10) == True
    assert rate_limiter.allow_requests("client_1",20) == True
    assert rate_limiter.allow_requests("client_1",30) == True
    assert rate_limiter.allow_requests("client_1",30) == True
    assert rate_limiter.allow_requests("client_1",50) == True
    assert rate_limiter.allow_requests("client_1",55) == False
   


def test_request_old_requests():
    rate_limiter = SlidingWindowRateLimiter(5,60)
    assert rate_limiter.allow_requests("client_1",10) == True
    assert rate_limiter.allow_requests("client_1",20) == True
    assert rate_limiter.allow_requests("client_1",30) == True
    assert rate_limiter.allow_requests("client_1",30) == True
    assert rate_limiter.allow_requests("client_1",50) == True
    assert rate_limiter.allow_requests("client_1",55) == False
    assert rate_limiter.allow_requests("client_1",75) == True