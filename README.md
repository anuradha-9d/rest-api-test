# rest-api-test

The purpose of this project is to demo the testing of rest api's in python.

Github rest api is used for this demo. This is an example of one of the github rest api's.

Performing a get on this url will retrieve all the publicly available for user "anuradha-9d"

For invoking Rest-API's requests module has been used, ConfigParser module has been used for reading the config settings and test data.

https://api.github.com/users/anuradha-9d/gists


#Install Instructions

Clone the github project
```
git clone https://github.com/anuradha-9d/rest-api-test.git
```

Install the python modules

```
cd rest-api-test
pip install -r requirements_dev.txt
```

Run unit tests

```
cd tests
python -m unittest -v test_rest-api-test
```
