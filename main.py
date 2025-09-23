import scraper
from datetime import datetime

bustype = input("Which Bus Timetable would you like?: ")
busday = input("What day would you like the timetable for? (YYYY-MM-DD Format): ")
url = f"https://www.morebus.co.uk/services/WDBC/{bustype}?date={busday}&direction=outbound&all=on"

timetable = scraper.getBusInfo(url)
stops = [stop.strip() for stop in timetable]

for i, stop in enumerate(timetable.keys(), start=1):
    print(f"{i}, {stop.strip()}")

start_choice = int(input("Which Bus stop do you want to start at?: ")) - 1
for i, stop in enumerate(timetable.keys(), start=1):
    print(f"{i}, {stop.strip()}")
end_choice = int(input("Which bus stop do you want to end at?: ")) - 1

start_stop = stops[start_choice]
end_stop = stops[end_choice]

if end_choice < start_choice:
    url = f"https://www.morebus.co.uk/services/WDBC/{bustype}?date={busday}&direction=inbound&all=on"
    timetable = scraper.getBusInfo(url)
    stops = [stop.strip() for stop in timetable]
    start_choice = stops.index(start_stop)
    end_choice = stops.index(end_stop)

user_time = input("What time do you want to be at your final stop by? (HH:MM Format): ")
end_time = datetime.strptime(user_time, "%H:%M").time()
final_stop_times = timetable[stops[end_choice]]

closest_time = None
closest_index = None
for i, t in enumerate(final_stop_times):
    if not t:
        continue
    bus_time = datetime.strptime(t, "%H:%M").time()
    if bus_time <= end_time:
        closest_time = bus_time
        closest_index = i

if closest_time:
    start_time = timetable[stops[start_choice]][closest_index]
    print(f"Take the {start_time} from {start_stop} to end up at {end_stop} at {closest_time}")
else:
    print("There are no buses available for this time. Try a different time")
