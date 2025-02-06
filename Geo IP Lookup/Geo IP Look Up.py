import tkinter as tk
import requests

# Function to fetch the geolocation details
def get_geo_info():
    ip = entry_ip.get()
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    # Update the result label based on the API response
    if data["status"] == "fail":
        result_label.config(text="Invalid IP Address!")
    else:
        result = f"IP: {data['query']}\nCountry: {data['country']}\nRegion: {data['regionName']}\nCity: {data['city']}\nISP: {data['isp']}\nLatitude: {data['lat']}\nLongitude: {data['lon']}"
        result_label.config(text=result)

# Create the main window
window = tk.Tk()
window.title("Geo-IP Lookup")

# Add an entry field for the IP address
entry_label = tk.Label(window, text="Enter IP Address:")
entry_label.pack(pady=10)
entry_ip = tk.Entry(window, width=30)
entry_ip.pack(pady=5)

# Add a button to trigger the lookup
button_lookup = tk.Button(window, text="Lookup", command=get_geo_info)
button_lookup.pack(pady=10)

# Add a label to display the result
result_label = tk.Label(window, text="", justify=tk.LEFT)
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
