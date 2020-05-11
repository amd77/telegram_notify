import datetime
import logging
import os
import tempfile
from decouple import config
from .bot import send_message, send_document, BOT_ENABLED

BOT_MODE = config("BOT_MODE", default="simple")


def request_format(request):
    def line(attr, value): return "{}: {}\n".format(attr.upper(), value)

    s = line('URI', request.get_raw_uri())
    for attr in ['method', 'user']:
        s += line(attr, getattr(request, attr))
    for attr in ['REMOTE_ADDR', 'HTTP_REFERER']:
        s += line(attr, request.META.get(attr, "-"))
    s += line('DATE', datetime.datetime.now())
    return s


def record_format_and_send(record, s):
    exceptionname = record.exc_info[0].__name__ + "_" if record.exc_info else ""
    dirname = tempfile.mkdtemp()
    filename = "{}{}.txt".format(exceptionname, datetime.datetime.now().strftime("%y%m%d_%H%M%S"))
    fullname = os.path.join(dirname, filename)
    open(fullname, "w").write(s)
    send_document(record.request.get_raw_uri(), fullname)
    os.unlink(fullname)
    os.rmdir(dirname)


class TelegramHandler(logging.Handler):
    def emit(self, record):
        s = self.format(record)
        if hasattr(record, 'request'):
            s = request_format(record.request) + "\n" + s
            if BOT_MODE == "document":
                record_format_and_send(record, s)
                return
        send_message(s)


def logging_config(level='ERROR', filename=None, **kwargs):
    base = {
        'version': 1,
        'disable_existing_loggers': False,
    }
    formatters = {}
    handlers = {}
    loggers = {}
    if filename:
        formatters['verbose'] = {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'
        }
        handlers['file'] = {
            'level': level,
            'class': 'logging.FileHandler',
            'filename': filename,
            'formatter': 'verbose',
        }
    if BOT_ENABLED:
        handlers['telegram'] = {
            'level': level,
            'class': 'telegram_notify.log.TelegramHandler',
        }
    if not kwargs:
        kwargs = {'': level}
    for path, level in kwargs.items():
        loggers[path] = {
            'handlers': list(handlers.keys()),
            'level': level,
            'propagate': True,
        }
    if formatters:
        base['formatters'] = formatters
    if handlers:
        base['handlers'] = handlers
    if loggers:
        base['loggers'] = loggers
    return base
