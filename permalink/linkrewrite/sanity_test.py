'''
    Created on Jun 22, 2013

    @author:  pgarnaut
'''

import requests
test_case_number = 0

def test_case(fn):
    def wrapped(*args, **kwargs):
        global test_case_number
        res = fn(*args, **kwargs)
        print "[%d] test case \"%s\"" % (test_case_number, fn.__name__),
        test_case_number += 1
        print "passed" if res else "failed"
        
    return wrapped

class SanityTest():
    def __init__(self):
        self.base_url = "http://localhost:8000/link/"
        self.link_name = ""
        self.test_payload = {"foo": "bar", "bob":[1,2,6]}
        self.test_redirect = 'http://www.google.com.au'
        
    @test_case
    def create(self):
        resp = requests.post(self.base_url, data=self.test_payload, headers={'redirect_url':self.test_redirect})
        if resp.status_code != 200:
            return False
        else:
            self.link_name = resp.content
            return True
        
    @test_case
    def get(self):
        print "GET: %s" % self.link_name
        resp = requests.get(self.base_url + self.link_name)
        if resp.status_code != 200:
            return False
        else:
            return True

class BrutalTest():
    def __init__(self):
        self.base_url = "http://localhost:8000/link/"
        self.brutality = 1000
        self.first_link = ""
        self.last_link = ""
        
    def create(self):
        resp = requests.post(self.base_url)
        return resp.content if resp.status_code == 200 else None
    

        
    @test_case
    def run(self):
        self.first_link = self.create()
        self.second_link = self.create()
    
        if not self.first_link or not self.second_link:
            return False
        
        for i in xrange(self.brutality):
            if i % 10 == 0:
                # keep the first one fresh
                if requests.get(self.base_url + self.first_link).status_code != 200:
                    return False
                
                self.create()
                
        # second one should have expired by now
        if requests.get(self.base_url + self.second_link).status_code != 404:
            return False
        
    
if __name__ == "__main__":
    test = SanityTest()
    test.create()
    test.get()
    
    test = BrutalTest()
    test.run()
