# python-fastapi
a very fast to develop api


## Setup Venv
```
python3 -m venv venv
source venv/bin/activate
# now we are in the venv

pip3 install fastapi
pip3 install uvicorn
pip3 install pydantic

# or pip3 install -r requirements.txt

```

- GET request — /loggapi/v1/logs
- POST request — /loggapi/v1/log

### The POST request

To add a new "event" to the log, you need to post one.

```
{
     "appId": "7542a72b-b6eb-4b9d-a672-a8d82ad0dadf",
     "message": "This is my log message.",
     "logType": "Info",
     "logDate": "Now"
}
```