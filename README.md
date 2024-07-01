## FastAPI Geolocation and Greeting API

This [HNG](https://hng.tech/internship) project demonstrates a simple FastAPI application that retrieves a user's location (city) and temperature (based on IP address) and returns a personalized greeting message. I have hosted the API on Vercel [here](https://hello-api-fast.vercel.app/api/hello).

**Features:**

- Uses FastAPI for a clean and efficient API framework.
- Integrates IP Geolocation API (IP-API) to fetch location data.
- Retrieves current weather temperature using Open-Meteo API (optional).
- Personalizes the greeting message with a visitor name (provided as a query parameter).
- Handles potential errors and returns informative messages.

**Running the Application Locally:**

**Prerequisites:**

- Python 3.6+
- `uvicorn` (install using `pip install uvicorn`)
- `httpx` (install using `pip install httpx`)

**Steps:**

1. Clone the repository (if applicable).
2. Navigate to the project directory.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Access the API endpoint at http://localhost:8000/api/hello. You can optionally add a query parameter for the visitor name (e.g., http://localhost:8000/api/hello?visitor_name=John).

**API Endpoint:**
/api/hello (GET request)

**Response:**

```
JSON
{
  "client_ip": "user's IP address",
  "location": "city name (or 'unknown')",
  "temperature": "temperature in degrees Celsius (or 'unknown')",
  "greeting": "Hello, visitor_name!, the temperature is temperature degrees Celsius in location"
}
```

**Deployment:**

The vercel.json file is configured for deployment on Vercel. Refer to Vercel's documentation for specific deployment instructions.

**API Keys:**

The provided APIs (IP-API and Open-Meteo) might have usage limits or require API keys for enhanced features or accuracy. Review their documentation for proper usage guidelines.

**Further Enhancements:**

- Explore alternative IP geolocation and weather APIs.
- Integrate user authentication for personalized experiences.
- Add additional features such as weather forecasts or historical data.
