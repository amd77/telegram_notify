# telegram\_notify

Django application for sending messages and error logging to telegram channel via bot

Requirements: requests, python-decouple


## Installation

Add to `requirements.txt` the following line:

`-e git+https://github.com/amd77/telegram_notify.git#egg=telegram_notify`

Then do `pip install -r requirements.txt`

## Configuration

Required: Talk to @botfather and create a new bot, give it a name, and save http api key in the file `.env` this way:
```
BOT_TOKEN = "uid:hash_by_botfather"
```

Required: Get the chatid(s) of the user or group or channel you want to talk. And add to `.env` this way:
```
BOT_CHATIDS = "chatid1,chatid2,..."
```

Optional: Add to `.env` if you want to send simple messages or documents with exception inside
```
BOT_MODE = "document"  # or "simple"
```

Not needed: Add to `.env` if you want to send messages to another api
```
BOT_URL = "https://api.telegram.org"  # default value
```

Required: In `your_application/settings.py` add `'telegram_notify'` to your `INSTALLED_APPS` and this lines:

```
from telegram_notify.log import logging_config
LOGGING = logging_config()
```

In `your_application/urls.py` add to the `urlpatterns` a test url that raises a ZeroDivisionError (only if you are logged in as root).

```
url(r'^test/', include('telegram_notify.urls')),
```


## Using

You can test the system using this management command, that :

```
./manage.py send_test_message
```

If you want to send a message, do the following:

```
from telegram_notify.bot import send_message
send_message("A useful message")
```

If you want to send a document, do the following:

```
from telegram_notify.bot import send_document
send_document("Caption", filename)
```

## Useful

In nginx use the following to pass remote hostname and client ip address:

```
location / {
	proxy_pass http://localhost:8000/;
	proxy_set_header Host            $host;
	proxy_set_header X-Real-IP       $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```
