

try:
    from config_local import config_db
except ImportError:
    config_db = {
        'user': 'user',
        'password': 'password',
        'host': '127.0.0.1',
        'database': 'piwik',
        'raise_on_warnings': True
    }


try:
    from config_local import config_output
except ImportError:
    config_output = [
        {
            "site_id": 0,
            "webhook": "https://www.example.com",
            "template": "default.tpl"
        }
    ]
