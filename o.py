import requests

def get_location(api_key, bssid, signal_strength):
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + api_key

    payload = {
        "wifiAccessPoints": [
            {
                "macAddress": bssid,
                "signalStrength": signal_strength,
                
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        location_data = response.json()
        return location_data.get("location", {})
    else:
        print(f"Geolocation API request failed with status code: {response.status_code}")
        return None

if __name__ == "__main__":
    # Replace with your Google Maps API key and Wi-Fi information
    google_maps_api_key = "AIzaSyAlhegMEoYyUUJVjl2vvwmLrY9vw4bWn5o"
    wifi_bssid = "22:6A:4F:BD:19:6A"
    wifi_signal_strength = -39  # Replace with actual signal strength in dBm
    #wifi_signal_to_noise_ratio = 40  # Replace with actual signal-to-noise ratio

    location = get_location(
        api_key=google_maps_api_key,
        bssid=wifi_bssid,
        signal_strength=wifi_signal_strength,
       # signal_to_noise_ratio=wifi_signal_to_noise_ratio
    )

    if location:
        print("Geolocation Information:")
        print("Latitude:", location.get("lat"))
        print("Longitude:", location.get("lng"))
        print("Accuracy:", location.get("accuracy"))
    else:
        print("Failed to retrieve geolocation information.")
###-0.982869,37.0775704