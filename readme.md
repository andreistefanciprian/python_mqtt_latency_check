
## Create Python virtual environment
```
# create python3 virtual env
python3 -m venv .env

# activate environment
source .env/bin/activate

# install mqtt client library
pip install paho-mqtt

# get list of installed packages inside virtual environment in requirements.txt file
pip freeze > requirements.txt
```

## Run python script

```
# create python3 virtual env
python3 -m venv .env

# install pip packages
pip install -r requirements.txt

# execute python script
python main.py
```
