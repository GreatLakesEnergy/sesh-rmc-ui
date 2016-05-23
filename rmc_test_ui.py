from rmc_app_ui import app

import os
import redis
from redis import Redis
import unittest

r =redis.Redis(host="127.0.0.1",port="6379" )

class RmcUiTest(unittest.TestCase):
  
    def setUp(self):
        r.set('uptime','30')
        r.set('eth_stat','ethactive')
        r.set('wlan','active')
        r.set('basedata','msg')

    def tearDown(self):
        r.flushdb()

    def test_main(self):
        tester = app.test_client(self)

        response = tester.get('/')
        self.assertEqual(response.status_code ,200)

if __name__ =="__main__":
    unittest.main()

