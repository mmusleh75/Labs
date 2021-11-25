import http.client

conn = http.client.HTTPSConnection("us-real-estate.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "us-real-estate.p.rapidapi.com",
    'x-rapidapi-key': "42aaba6c1bmsh319b0e840d3943bp1ac941jsnb9d4a668df36"
    }

conn.request("GET", "/v2/for-sale?offset=0&limit=42&state_code=KS&city=OLATHE&location=66062&sort=newest&price_max=265000&beds_min=3&baths_min=2&property_type=single_family&no_hoa_fee=true", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
