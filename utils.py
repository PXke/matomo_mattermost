
import datetime
import mysql.connector
from config import config_db


def get_data_until(id_site, date):
    """Return a list of row for the site until the date specified."""
    cnx = mysql.connector.connect(**config_db)
    cursor = cnx.cursor()

    query = (
        "SELECT * FROM piwik_log_visit WHERE visit_first_action_time > %s AND idsite=%s ")

    cursor.execute(query, (date, id_site))
    data_to_return = list(cursor)
    cnx.close()

    return data_to_return


def get_site_name(id_site):
    """Return a site name based on site id."""

    cnx = mysql.connector.connect(**config_db)
    cursor = cnx.cursor()

    query = ("SELECT * FROM piwik_site WHERE idsite=%s")

    cursor.execute(query, (id_site,))
    try:
        site_name = list(cursor)[0][1]
    except IndexError:
        site_name = None
    finally:
        cnx.close()

    return site_name


def render_default_template(id_site):
    """Get the data needed for the default template."""
    data = {}
    data["site_name"] = get_site_name(id_site)
    data["id_site"] = id_site
    yesterday = datetime.datetime.now() - datetime.timedelta(hours=24)
    rows_yesterday = get_data_until(id_site, yesterday)
    last_week = datetime.datetime.now() - datetime.timedelta(hours=24*7)
    rows_last_week = get_data_until(id_site, last_week)

    data["count_today"] = len(rows_yesterday)
    data["count_last_week"] = len(rows_last_week)/7
    data["difference_avg"] = data["count_today"] - data["count_last_week"]
    if data["difference_avg"] < 0:
        data["chart"] = ":chart_with_downwards_trend:"
    else:
        data["chart"] = ":chart_with_upwards_trend:"
    tpl = ""
    with open("templates/default.tpl") as template:
        tpl = template.read()

    return tpl.format(**data)
