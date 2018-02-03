## flask_explore
[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)

Flask explore

### Setup for linux
```
git clone https://github.com/polieter/flask_explore.git
cd /flask_explore
pip install -r requirements.txt

python database.py

mkdir instance
echo SQLALCHEMY_DATABASE_URI = 'sqlite:///<full path to data base>' >> instance/config.py
echo SQLALCHEMY_TRACK_MODIFICATIONS = False >> instance/config.py
echo DEBUG = True >> instance/config.py
echo SECRET_KEY = '<-------this_is_a_secret_key_xD------->' >> instance/config.py

python run.py
```