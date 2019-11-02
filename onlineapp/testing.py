import time
from threading import Thread
import requests
from requests.auth import HTTPBasicAuth
from random import randint
import json


success = 0
failed = 0

class RequestGenerator(Thread):
    def __init__(self, val):
        ''' Constructor. '''
        Thread.__init__(self)
        self.val = val

    def detail_college(self, college_id):
        url = "http://127.0.0.1:8000/onlineapp/api/colleges/"
        response = requests.get(url, auth=HTTPBasicAuth('preethialuru', 'spreethis'))
        if response.status_code != 200:
            print("request failed in detail college ", response.status_code)
            return []

        return json.loads(response.text)

    def run(self):
        global success
        global failed
        try:
            start = time.time()
            colleges = self.list_colleges()
            if len(colleges) > 0:
                college_id = randint(1, len(colleges))
                college_detail = self.detail_college(college_id)
                print(college_detail)
            end = time.time()
            print("Request took ", (end - start), " to complete for ", self.val, " iteration")
            success = success + 1
        except Exception as e:
            print("Caught exception ", e, " in handling of request ", self.val)
            failed = failed + 1


    def list_colleges(self):
        url = "http://127.0.0.1:8000/onlineapp/api/colleges"
        response = requests.get(url, auth=HTTPBasicAuth('preethialuru', 'spreethis'))
        if response.status_code != 200:
            print("request failed in list college ", response.status_code)
            return []

        return json.loads(response.text)


# Run following code when the program starts
if __name__ == '__main__':
    # Use 10 parallel threads
    request_generators = []
    thread_count = 12

    for i in range(0, thread_count):
        request_generator = RequestGenerator(i)
        request_generators.append(request_generator)
        request_generator.setName("Request Generator "+ str(i))
        request_generator.start()

    for i in range(0, thread_count):
        request_generators[i].join()

    print('Completed activity')
    print('Total threads ', thread_count, ' success ', success, ' failed ', failed )
