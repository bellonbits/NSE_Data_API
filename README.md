# NSE Data API

A FastAPI-based web service that fetches and serves Nairobi Securities Exchange (NSE) stock market data in JSON format. Deployed on Vercel for high availability and global access.

## 🚀 Features

- **Real-time NSE Data**: Fetches live stock market data from NSE
- **JSON API**: Clean, structured JSON responses
- **Error Handling**: Comprehensive error handling with proper HTTP status codes
- **Data Cleaning**: Automatically handles NaN/null values and converts them to 0
- **Serverless**: Deployed on Vercel for optimal performance and scalability
- **CORS Enabled**: Accessible from web applications

## 📡 API Endpoints

### Base URL
```
https://your-app.vercel.app
```

### Endpoints

#### `GET /`
Returns API information and available endpoints.

**Response:**
```json
{
  "message": "NSE Data API is running",
  "endpoints": ["/nse"]
}
```

#### `GET /api/nse`
Fetches current NSE stock market data.

**Response:**
```json
[
  {
    "Company": "Equity Group Holdings Plc",
    "Price": 45.25,
    "Change": 1.25,
    "Volume": 125000,
    "Market Cap": 0
  },
  ...
]
```

## 🛠️ Technology Stack

- **FastAPI**: Modern, fast Python web framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Requests**: HTTP library for fetching data
- **Vercel**: Serverless deployment platform

## 📁 Project Structure

```
nse-api/
├── api/
│   └── index.py          # Main FastAPI application
├── vercel.json           # Vercel deployment configuration
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🚀 Local Development

### Prerequisites
- Python 3.9+
- pip

### Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/bellonbits/NSE_Data_AP](https://github.com/bellonbits/NSE_Data_AP)
   cd nse-api
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run locally:**
   ```bash
   uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the API:**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - NSE Data: http://localhost:8000/api/nse

## 🌐 Deployment on Vercel

### Prerequisites
- Node.js (for Vercel CLI)
- Git
- Vercel account

### Deploy Steps

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```

3. **Follow the prompts:**
   - Set up and deploy
   - Choose your project settings
   - Your API will be live at the provided URL

### Environment Variables (if needed)
```bash
vercel env add VARIABLE_NAME
```

## 📊 Data Source

The API fetches data from the official NSE data provider at `https://afx.kwayisi.org/nse/`. The data includes:

- Company names
- Current stock prices
- Price changes
- Trading volumes
- Market capitalization
- Other relevant financial metrics

## 🔧 Configuration

### vercel.json
```json
{
  "functions": {
    "api/index.py": {
      "runtime": "python3.9"
    }
  },
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/index.py"
    },
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

## ⚠️ Error Handling

The API includes comprehensive error handling:

- **503 Service Unavailable**: When unable to fetch data from the source
- **404 Not Found**: When the required data table is not found
- **500 Internal Server Error**: For unexpected server errors
- **Timeout**: 30-second timeout for external requests

## 🔒 Data Processing

- **NaN/Null Handling**: All NaN, null, and empty values are converted to `0`
- **Data Validation**: Ensures all data is JSON-serializable
- **Column Cleaning**: Strips whitespace from column names
- **Type Conversion**: Automatically converts numeric data types

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you have any questions or need support:

- Create an issue in this repository
- Contact: [petergatitu61@gmail.com]

## 🔄 API Usage Examples

### JavaScript/Fetch
```javascript
fetch('https://your-app.vercel.app/api/nse')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### Python/Requests
```python
import requests

response = requests.get('https://your-app.vercel.app/api/nse')
data = response.json()
print(data)
```

### cURL
```bash
curl -X GET "https://your-app.vercel.app/api/nse" \
     -H "accept: application/json"
```

## 📈 Performance

- **Response Time**: Typically < 2 seconds
- **Availability**: 99.9% uptime (Vercel SLA)
- **Rate Limits**: Subject to Vercel's function execution limits
- **Caching**: Consider implementing caching for production use

## 🔮 Future Enhancements

- [ ] Data caching mechanism
- [ ] Historical data endpoints
- [ ] Real-time WebSocket connections
- [ ] Authentication and rate limiting
- [ ] Multiple data sources
- [ ] Data visualization endpoints
- [ ] Email/SMS alerts for price changes

---

Made with ❤️ for the Kenyan financial community
