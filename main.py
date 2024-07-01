from fastapi import FastAPI, Request
import httpx

app = FastAPI()

async def get_geodata(request: Request):
    client_ip = request.client.host

    try:
        async with httpx.AsyncClient() as client:
            geo_response = await client.get(f'http://ip-api.com/json/{client_ip}')
            print('geo_response', geo_response)
            geo_data = geo_response.json()
            print('geodata:', geo_data)
            location = geo_data.get('city', 'your city')
            lat = geo_data.get('lat')
            lon = geo_data.get('lon')
            
            temp_response = await client.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true')
            temp_data = temp_response.json()
            temperature = temp_data['current_weather']['temperature']
            
        return { 'client_ip': client_ip, 'location': location, 'temperature': temperature}
    
    except Exception as e:
        return { 'client_ip': client_ip, 'location': 'unknown', 'temperature': 'unknown', 'error': str(e) }

@app.get("/api/hello")
async def hello(request: Request, visitor_name: str = "Guest"):
    try:
        geo_response = await get_geodata(request)

        response = {
            "client_ip": geo_response['client_ip'],
            "location": geo_response['location'],
            "greeting": f"Hello, {visitor_name}!, the temperature is {geo_response['temperature']} degrees Celsius in {geo_response['location']}"
        }
        return response
    except Exception as e:
        return {"error": "Error fetching data: " + str(e)}, 500

# Uncomment the below lines if you want to run this script locally
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
