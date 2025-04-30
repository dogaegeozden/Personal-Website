# LIBRARIES
from django.test import TestCase
from http import HTTPStatus

# Create your tests here.

class RobotsTest(TestCase):

    def test_get(self):
        """A function tests get requests on /robots.txt"""

        # Important: You need to modify visitors_user_agent.py file and return a reqular string instead of user's user agent to be able to run this test. Don't try to capture user's user-agent while running this test.
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], "User-Agent: *")

    def test_post(self):
        """A function which tests post requests on /robots.txt"""
        
        response = self.client.post("/robots.txt")
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)
