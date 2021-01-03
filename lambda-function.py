import requests
import json
from icalevents import icalevents
import pytz
from datetime import datetime

def convert_timestamp_in_datetime_utc(timestamp_received):
	dt_naive_utc = datetime.utcfromtimestamp(timestamp_received)
	return dt_naive_utc.replace(tzinfo=pytz.utc)

def lambda_handler(event, context):
	try:
		cal_url = event['cal_url']
		window1_start = event['window1'] + 1
		window1_end = window1_start + 86398
		window2_start = event['window2'] + 1
		window2_end = window2_start + 86398

		window1_start_date = convert_timestamp_in_datetime_utc(window1_start)
		window1_end_date = convert_timestamp_in_datetime_utc(window1_end)
		window2_start_date = convert_timestamp_in_datetime_utc(window2_start)
		window2_end_date = convert_timestamp_in_datetime_utc(window2_end)

		cal_data = requests.get(cal_url).text
		cal_bytes = str.encode(cal_data)

		window1_events = icalevents.events(string_content=cal_bytes,start=window1_start_date,end=window1_end_date)
		window2_events = icalevents.events(string_content=cal_bytes,start=window2_start_date,end=window2_end_date)

		#return {
		#    "statusCode": 200,
		#    "headers": {
		#        "Content-Type": "application/json"
		#    },
		#    "body": json.dumps({
		#        "window1": len(window1_events),
		#        "window2": len(window2_events)
		#    })
		#}
	except:
		return {
			"error": True,
			"window1": 0,
			"window2": 0
		}

	else:
		return {
			"error": False,
			"window1": len(window1_events),
			"window2": len(window2_events)
		}
