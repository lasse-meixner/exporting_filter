import pandas as pd

print("Reading export data...")
# read export.csv
try:
    appData = pd.read_csv("export.csv")
except FileNotFoundError:
    print("export.csv not found. Please place app export into this file and name it 'export.csv' before running.")
    exit()

# cast date column to datetime and get minimum date
appData["date"] = pd.to_datetime(appData["date"])
min_date = appData["date"].min()

first_n = 200000

while True:
    print("Reading health data...")
    # read apple health csv and filter on all values after the min_date
    try:
        health = pd.read_csv("apple_health_export.csv",nrows=first_n)
    except FileNotFoundError:
        print("apple_health_export.csv not found. Please place apple health export into this file and name it 'apple_health_export.csv' before running.")
        exit()

        
    health["start"] = pd.to_datetime(health["startDate"])

    # filter on all values after the min_date
    new = health[health["start"]>=min_date].reset_index(drop=True)

    if len(new)<len(health):
        # save new filtered data to csv
        print("Saving new health data...")
        new.to_csv("health_filtered.csv",index=False)
        break
    else:
        first_n += 200000
        print("Increasing first_n to",first_n)