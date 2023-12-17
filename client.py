from jodev_emailpy.errors import EmailPyAPIError
from jodev_emailpy.utils import retry
from requests import post, get

class EmailPy:
    """Python SDK for EmailJS API."""

    def __init__(self, public_key):
        """
            Initializes the EmailJS client.

            Args:
                public_key (str): Your EmailJS public key.
        """
        self.public_key = public_key
        self.base_url = "https://api.emailjs.com/api/v1.0"
        self.history_url = "https://api.emailjs.com/api/v1.1"
        self.access_token = ""

    @retry(max_retries=3)
    def send(self, service_id, template_id, template_params, access_token=None):
        """
        Sends an email using the EmailJS API with automatic retry.

        Args:
            service_id (str): ID of the service used to send the email.
            template_id (str): ID of the email template.
            template_params (dict): Dictionary containing template parameters.
            access_token (str, optional): Your EmailJS access token.

        Returns:
            requests.Response: The API response object.
        """

        if self.public_key == "" or self.public_key == None or len(self.public_key) <= 1 :
            raise EmailPyAPIError(400, "public key is required to have been set before recieving email")
        
        url = f"{self.base_url}/email/send"
        headers = {"Content-Type": "application/json"}
        
        data = {
            "service_id": service_id,
            "template_id": template_id,
            "user_id": self.public_key,
            "template_params": template_params, 
            }
        
        if access_token:
            headers["Authorization"] = f"Bearer {access_token}"
        response = post(url, headers=headers, json=data)
        if not response.ok:
            raise EmailPyAPIError(response.status_code, response.text)
        
        return response
    
    def setAccessToken(self, access_token : str) -> None:
        '''
            access_token (string, required) : This is the private key of your emailjs account
    
        '''
        self.access_token = access_token 

    def setPublicKey(self, public_key : str) -> None:
        '''
            access_token (string, required) : This is the public key of your emailjs account
    
        '''
        self.public_key = public_key 

    @retry(max_retries=3)
    def get_history(self, page=1, count=10, access_token = ""):
        """
            Gets a list of email history records.
			Args:
                page (int, optional): The page number to retrieve. Defaults to 1.
                count (int, optional): The number of records per page. Defaults to 10.
                

			Returns:
				dict: The API response containing history records.
        """
        url = f"{self.history_url}/history"
        if access_token != "":
            self.setAccessToken(access_token)

        if self.access_token == "" or len(self.access_token) <= 1:
            raise EmailPyAPIError(400, "access token is required in order to retrieve email history")
        
        params = {
	 		"user_id": self.public_key,
			"page": page,
			"count": count,
            "accessToken":self.access_token
		}

        response = get(url,  params=params)
        
        if not response.ok:
            raise EmailPyAPIError(response.status_code, response.text)
        
        return response