# **Exchange Rates App**

## Tech Stack
1. Django 2.1.5
2. Python 3.6.6
3. OS - Ubuntu 18.04

## Installation (for Debian based Linux/OS X)
In order to install the project, please follow the steps given below:

1. `cd` into the project root directory (`currency_converter`)
2. Create a `virtualenv` environment.
3. Run `pip install -r requirements.txt`
4. Run `python manage.py runserver`

## Usage
Using a browser or any other tool like Postman or Putty, please hit the following URL:
http://localhost:8000/converter/convert/?source=USD&target=INR&amount=200

You can use any **ISO 4217** currency value for query parameters that are `source`, `target`. For `amount` you can enter any numerical value.