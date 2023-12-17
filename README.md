
# jodev_emailpy
**A Python package that helps you send and recieve email directly using emailjs restful service**

## Getting Started
To install into your python environment use 
`pip install jodev_emailpy`

On successfull installation , you are ready to start using jodev_emailpy to start recieving and sending email directly from your client side application no backend server needed

# Useage
To send a message to your configured email
```python
from jodev_emailpy import EmailPy

PUBLIC_KEY :str = "YOUR-PUBLIC-KEY-FROM-EMAILJS"
SERVICE_ID : str =  "YOUR-SERVICE-ID-FROM-EMAILJS"
TEMPLATE_ID :str = "YOUR-TEMPLATE-ID-FROM-EMAILJS"
TEMPLATE_PARAMS : dict = {
    # customize to fit as per your template variables requirement e.g
    "email_id" : "jodek@gmail.com",
    "message": "hello test mssg"
    
}
# input your public_key to initialize the client
client = EmailPy(PUBLIC_KEY)

client.send(service_id=SERVICE_ID,  template_id=TEMPLATE_ID, 
template_params=TEMPLATE_PARAMS)

```

To retrieve a list of email history 

```python
ACCESS_TOKEN = "YOUR-ACCESS-TOKEN-SECRET-KEY"
response = client.get_history(access_token=ACCESS_TOKEN)
```
Other optional arguments to pass to get_history method are :
* count : int  #this is the count of email history to retrieve
* page : int default is 1 . this helps for pagination

> note access token can then be omitted for successive call of get_history()

if response status is 200 without error you should be able to retrieve email history
```python
print(response.json()['rows'])
```

> *ensure you have signed up on emailjs website so as to have access to credentials needed*. if not, here is their website link to sign up [https://dashboard.emailjs.com/sign-up](https://dashboard.emailjs.com/sign-up)
