
import requests

def get_weather_data():
    api_key = "b6907d289e10d714a6e88b30761fae22"
    base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
    city = "London,us"

    response = requests.get(f"{base_url}?q={city}&appid={api_key}")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def get_temp_on_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["main"]["temp"]
    return None

def get_wind_speed_on_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["wind"]["speed"]
    return None

def get_pressure_on_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["main"]["pressure"]
    return None

def main():
    data = get_weather_data()
    if data is None:
        return

    while True:
        print("\nMenu:")
        print("1. Get temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date_input = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_temp_on_date(data, date_input)
            if temperature is not None:
                print(f"Temperature on {date_input}: {temperature}°C")
            else:
                print("Date not found in the forecast.")

        elif choice == "2":
            date_input = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed_on_date(data, date_input)
            if wind_speed is not None:
                print(f"Wind Speed on {date_input}: {wind_speed} m/s")
            else:
                print("Date not found in the forecast.")

        elif choice == "3":
            date_input = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure_on_date(data, date_input)
            if pressure is not None:
                print(f"Pressure on {date_input}: {pressure} hPa")
            else:
                print("Date not found in the forecast.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
