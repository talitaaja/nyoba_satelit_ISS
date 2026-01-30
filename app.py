import requests
import time
from datetime import datetime

API_URL = "http://api.open-notify.org/iss-now.json"

def get_iss_location():
    try:
        response = requests.get(API_URL, timeout=5)
        data = response.json()

        if data["message"] == "success":
            lat = float(data["iss_position"]["latitude"])
            lon = float(data["iss_position"]["longitude"])
            timestamp = data["timestamp"]

            waktu = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            return lat, lon, waktu
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None


def main():
    print("🌍 ISS Realtime Location Tracker")
    print("Tekan CTRL+C untuk berhenti\n")

    while True:
        result = get_iss_location()

        if result:
            lat, lon, waktu = result
            print(f"Waktu (UTC) : {waktu}")
            print(f"Latitude    : {lat:.6f}°")
            print(f"Longitude   : {lon:.6f}°")
            print("-" * 40)
        else:
            print("Gagal ambil data ISS")

        time.sleep(5)  # update tiap 5 detik


if __name__ == "__main__":
    main()
