# CSFlix Web Application

## Description

A Web application that demonstrates use of Python's Flask framework. The application makes use of libraries such as the Jinja templating library and WTForms. Architectural design patterns and principles including Repository, Dependency Inversion and Single Responsibility have been used to design the application. The application uses Flask Blueprints to maintain a separation of concerns between application functions. Testing includes unit and end-to-end testing using the pytest tool. 

## Installation

**Installation via requirements.txt**

```shell
$ cd Assignment-2
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:Assignment-2' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution and testing from virtual environment

From the *Assignment-2* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

**Running the application**

````shell
$ flask run
```` 
--Please note--

If web app seems to be styled incorrectly, it may be that it is the web browser that is caching the stylesheet.
If you're using Chrome, you can disable caching: click the dot dot dot button (top right of window), more tools, developer tools, network, disable cache.  

**Running all tests**

````shell
$ python -m pytest
```` 

## Configuration

The *Assignment-2/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.


## Testing

Testing requires that file *Assignment-2/tests/conftest.py* be edited to set the value of `TEST_DATA_PATH`. You should set this to the absolute path of the *Assignment-2/tests/data* directory. 

E.g. 

`TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'camer', 'Desktop', 'A place to save stuff', 'compsci235', 'Assignment-2', 'tests', 'data')`

assigns TEST_DATA_PATH with the following value (the use of os.path.join and os.sep ensures use of the correct platform path separator):

`C:\Users\camer\Desktop\A place to save stuff\Assignment-2\tests\data`

You can then run tests from within PyCharm.

 