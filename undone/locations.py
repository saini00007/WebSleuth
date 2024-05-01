import geocoder
from timezonefinder import TimezoneFinder

def get_location_info(url):
    g = geocoder.arcgis(url)
    tf = TimezoneFinder()

    timezone = tf.timezone_at(lng=g.lng, lat=g.lat)
    
    location_info = {
        "Server Location": ", ".join(filter(None, [g.city, g.state, g.country])),
        "Country": g.country,
        "Timezone": timezone if timezone else "Unknown",
        "Languages": g.language,
        "Currency": g.currency
    }
    
    return location_info

if __name__ == "__main__":
    url = input("Enter URL: ")
    info = get_location_info(url)
    for key, value in info.items():
        print(f"{key}: {value}")
