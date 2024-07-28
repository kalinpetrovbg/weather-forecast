import requests
from datetime import datetime

api_key = "57858e29f5c6441a58ad0170310986a3"


def normalize_temp(temperature):
    temperature = temperature / 10
    temperature = round(temperature)
    return temperature


def get_next_n_records(data, n):
    return {k: data[k] for k in list(data)[:n]}


def get_data(location, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    data_list = data["list"]

    new_data = {}

    for record in data_list:
        datetime_str = record["dt_txt"]
        date_object = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        formatted_date = date_object.strftime("%d %b")

        entry = {
            "time": datetime_str[11:16],
            "temperature": normalize_temp(record["main"]["temp"]),
            "feels_like": normalize_temp(record["main"]["feels_like"]),
            "humidity": record["main"]["humidity"],
            "image": f"images/{record['weather'][0]['main'].lower()}.png"
        }

        if formatted_date not in new_data:
            new_data[formatted_date] = [entry]
        else:
            new_data[formatted_date].append(entry)

    return get_next_n_records(new_data, days)


if __name__ == "__main__":
    print(get_data("Sofia", 1))