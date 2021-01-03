import requests
from icalevents import icalevents
import dateutil.parser
import dateutil.tz
from timeit import default_timer as timer

start_time = timer()

cal_url = "https://calendar.google.com/calendar/ical/c_pdnr66cqie3ldscaj5a2rb21h0%40group.calendar.google.com/private-f1075da9b4e5634cb3775640cea1e69b/basic.ics"

cal_data = requests.get(cal_url).text
cal_bytes = str.encode(cal_data)
print("got cal data")

start = dateutil.parser.parse('2020-12-24T00:00:00-05:00')
end = dateutil.parser.parse('2020-12-24T23:59:59-05:00')

today_events = icalevents.events(string_content=cal_bytes,start=start,end=end)
#today_events = icalevents.events(url=cal_url,start=start,end=end)

print(today_events)

start = dateutil.parser.parse('2020-12-25T00:00:00-05:00')
end = dateutil.parser.parse('2020-12-25T23:59:59-05:00')

tomorrow_events = icalevents.events(string_content=cal_bytes,start=start,end=end)
#tomorrow_events = icalevents.events(url=cal_url,start=start,end=end)

print(tomorrow_events)

end_time = timer()
print("Execution time: {}".format(end_time - start_time))