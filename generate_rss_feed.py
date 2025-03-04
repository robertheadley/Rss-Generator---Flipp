import json
import xml.etree.ElementTree as ET

# Path to the JSON file
json_file = "results.json"  # Ensure results.json exists in the repository
rss_file = "rss_feed.xml"

# Load the JSON data
with open(json_file, "r") as file:
    data = json.load(file)

# Create the RSS feed
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")

# Add channel details
ET.SubElement(channel, "title").text = "Coca-Cola Products Search Results"
ET.SubElement(channel, "link").text = "https://cdn-gateflipp.flippback.com"
ET.SubElement(channel, "description").text = "Search results for Coca-Cola products with photos"

# Add items to the RSS feed
for item in data.get("ecom_items", []):
    rss_item = ET.SubElement(channel, "item")
    ET.SubElement(rss_item, "title").text = item.get("name", "No Title")
    ET.SubElement(rss_item, "link").text = item.get("image_url", "")
    ET.SubElement(rss_item, "description").text = item.get("description", "No Description")
    ET.SubElement(rss_item, "price").text = f"${item.get('current_price', 'N/A')}"
    if "image_url" in item:
        image = ET.SubElement(rss_item, "enclosure", type="image/png")
        image.set("url", item["image_url"])

# Save the RSS feed to a file
rss_tree = ET.ElementTree(rss)
rss_tree.write(rss_file, encoding="utf-8", xml_declaration=True)
