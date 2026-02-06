import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Open-Meteo API (no key required)
URL = "https://api.open-meteo.com/v1/forecast?latitude=17.385&longitude=78.4867&hourly=temperature_2m,relative_humidity_2m,windspeed_10m"

response = requests.get(URL)
data = response.json()

temps = data['hourly']['temperature_2m'][:12]
humidity = data['hourly']['relative_humidity_2m'][:12]
wind_speed = data['hourly']['windspeed_10m'][:12]
times = [datetime.datetime.fromisoformat(t) for t in data['hourly']['time'][:12]]

plt.figure(figsize=(12,6))
sns.lineplot(x=times, y=temps, marker="o", label="Temperature (°C)")
sns.lineplot(x=times, y=humidity, marker="s", label="Humidity (%)")
sns.lineplot(x=times, y=wind_speed, marker="^", label="Wind Speed (m/s)")
plt.title("Weather Forecast (Hyderabad)")
plt.xlabel("Time")
plt.ylabel("Values")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
