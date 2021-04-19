
## Description

* mqtt publisher script used for publishing messages to mqtt topic.
* mqtt subscriber script used for publishing a response to all published messages and calculating min/max/avg latency for each publisher.

## Setup python environment

```bash
# create python3 virtual env
python3 -m venv .env

# activate python env
source .env/bin/activate

# install pip packages
pip install -r requirements.txt

# deactivate python env after running the publisher/subscriber scripts
deactivate
```

## Publish messages to mqtt topic
```bash
python publisher.py
```
Note: Initialize script multiple times, if multiple publishersare required.

## Subscribe to mqtt topic and calculate latency for published messages
```bash
python subscriber.py
```

Latency results will be displayed after script stops running in this format:
```bash
Subscriber-1 latency results - min:0.0147s max:0.0241s avg:0.0193s
Subscriber-2 latency results - min:0.0124s max:0.0301s avg:0.0192s
```
