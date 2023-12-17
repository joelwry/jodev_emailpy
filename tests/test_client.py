import unittest 
from jodev_emailpy.client import EmailPy
import os

# change this to your own personal as given from emailjs website
# you can hide your keys in your environment variable or paste it manually hence you remove os.environ.get and put in the actual value

PUBLIC_KEY = os.environ.get("EMAILJS_PUB_KEY") 
SERVICE_ID = os.environ.get("EMAILJS_SERVICE_ID") 
TEMPLATE_ID = os.environ.get("EMAILJS_TEMPLATE_ID")
ACCESS_TOKEN = os.environ.get("EMAILJS_ACCESS_TOKEN") 

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = EmailPy(PUBLIC_KEY)
        self.client.setAccessToken(ACCESS_TOKEN)
        
    def donot_test_send(self): 
        response = self.client.send(
            service_id=SERVICE_ID,  
            template_id=TEMPLATE_ID, 
            # customize to fit as required by your template id variables
            template_params={
                "email_id": "milli5ax@gmail.com",
                "message":'Hello! this is from emailpy service test',
                "username": "Emailpy",
                }
            )
        self.assertEqual(response.status_code, 200)

    def test_history(self):
        response = self.client.get_history(access_token=ACCESS_TOKEN)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertIsInstance(response.json()['rows'], list )
        print(response.json()['rows'])

if __name__ == "__main__": 
    unittest.main()
