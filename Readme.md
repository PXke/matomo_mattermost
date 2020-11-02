# Introduction

The idea of this code was to be able to output simple statistics from Matomo to mattermost channel. 

This is definitely not the best solution as it is not directly integrated into Matomo and it will work only with on-premise installations. 

It is a rudimentary script that query directly the database and post the content to a mattermost channel. 


# Installation


Clone the repository in `/opt` 

```sh
cd /opt
git clone https://github.com/PXke/matomo_mattermost.git
```


Then install a cron for example

```
sudo crontab -e
```

```
0 17 * * * cd /opt/matomo_mattermost/ && python3 main.py
```

Will get you the stats posted at 5pm. 


# Configuration

We recommend you to create a `config_local.py` file next to the `¢onfig` one. 

You need two variables: 
```python
    config_db = {
        'user': 'user',
        'password': 'password',
        'host': '127.0.0.1',
        'database': 'piwik',
        'raise_on_warnings': True
    }

    config_output = [
        {
            "site_id": 0,
            "webhook": "https://www.example.com",
            "template": "default.tpl"
        }
    ]
```

# To do

Ideally create a true plugin into Matomo, otherwise:

- [] Use a true templating library like Jinja2

- [] Add discovery of templates. 

- [] Add discovery of tokens and computation of values on the fly. 

- [] and more
