# weather
Basic weather App using Flask

1) install python https://www.python.org/downloads/

	to verify that you have python installed 

```
(base) C:\Users\Daisuke Shimizu>python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>_
```

2) Create a virtual environment

```
(base) C:\Users\Daisuke Shimizu>python3 -m venv venv
``` 
You can replace the second "venv" with a different name

3) Activate virtual environment

```
(base) C:\Users\Daisuke Shimizu>venv\Scripts\activate
(venv) (base) C:\Users\Daisuke Shimizu>_
```

4) install flask

```
(venv) (base) C:\Users\Daisuke Shimizu>pip install flask
```

Before running the app, set the FLASK_APP environment variable so Flask knows how to import the app

```
(venv) (base) C:\Users\Daisuke Shimizu>set FLASK_APP=microblog.py
```

Run Flask 

```
flask run
```

Then open the web browser and enter 
```
http://localhost:5000/
```
