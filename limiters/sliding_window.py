from flask import Flask, jsonify, request
from collections import deque



class SlidingWindowRateLimiter:

    def __init__(self, max_requests, window):
        self.clients = {}
        self.max_requests = max_requests
        self.window = window #in sec

    def check_client(self, client):
        #this checks if the client exists or not
        return client in self.clients
    
    def allow_requests(self, client, curr_request_time):
        #this returns weather a client is allowed to make request or not 

        if self.max_requests == 0:
            return False
        
        #  check if the client exists or not
        if not self.check_client(client):
            # client  do not exists, add the clinet to the dict
            self.clients[client] =  deque([curr_request_time])  
            return True        

        
        while self.clients[client] and ( curr_request_time - self.clients[client][0] > self.window):
            self.clients[client].popleft()

        if len(self.clients[client]) >= self.max_requests:
            return False
        # {"status": 429, "msg": "Rate limit reached"}
        else:
            self.clients[client].append(curr_request_time)
            return  True