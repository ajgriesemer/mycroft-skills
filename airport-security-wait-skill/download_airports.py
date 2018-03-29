import xml.etree.ElementTree, requests, hashlib

# Assign a variable for the TSA API endpoint for downloading all airport data
all_airports_url = "https://www.tsa.gov/data/apcp.xml"
all_airports_checksum_url = "https://www.tsa.gov/data/apcp.checksum.xml"

xml_response = requests.get(all_airports_url)

if xml_response.status_code != 200:
    raise Exception("Unable to download airports data.")

checksum_xml_response = requests.get(all_airports_checksum_url)

if checksum_xml_response.status_code != 200:
    raise Exception("Unable to download airports data checksum.")

checksum_response_tree = xml.etree.ElementTree.fromstring(checksum_xml_response.content)
checksum_response = checksum_response_tree[0][0].text

checksum = hashlib.md5(xml_response.content).hexdigest().upper()

if checksum == checksum_response:
    print("Checksum Confirmed")
else:
    raise Exception("Airports data file does not match checksum.")

airports = xml.etree.ElementTree.fromstring(xml_response.content)

airports_file_string = ""
for airport in airports:
    airports_file_string = airports_file_string + "\"" + airport.find(".//shortcode").text + "\"\n"

with open('vocab/en-us/Airports.voc', 'w') as output_file:
    output_file.write(airports_file_string)

