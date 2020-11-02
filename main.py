import mysql.connector
import datetime
import json
import requests


from config import config_output
from utils import render_default_template


content_per_webhook = {}
for c in config_output:
    if c["template"] == "default.tpl":
        content = render_default_template(c["site_id"])

    if c["webhook"] not in content_per_webhook:
        content_per_webhook[c["webhook"]] = content
    else:
        content_per_webhook[c["webhook"]] += content

for webhook in content_per_webhook:
    payload = {
      "username": "Matomo",
      "icon_url": "",  # noqa
      "text": content_per_webhook[webhook]
    }

    r = requests.post(webhook, json.dumps(payload))
