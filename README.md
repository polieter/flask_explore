## flask_explore
[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)

Flask explore

### Setup for linux
```
git clone https://github.com/polieter/flask_explore.git
pip install -r requirements.txt
cd /flask_explore
mkdir instance
python database.py
echo SQLALCHEMY_DATABASE_URI = 'sqlite:///<full path to data base>' >> instance/config.py
SQLALCHEMY_TRACK_MODIFICATIONS = False >> instance/config.py
DEBUG = True >> instance/config.py
SECRET_KEY = '<-------this_is_a_secret_key_xD------->' >> instance/config.py
python run.py
```