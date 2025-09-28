# api/index.py
from fastapi import FastAPI, HTTPException
import pandas as pd
import requests
import numpy as np
from typing import List, Dict, Any

app = FastAPI(title="NSE Data API", description="API to fetch NSE stock data")

@app.get("/")
def read_root():
    return {"message": "NSE Data API is running", "endpoints": ["/nse"]}

@app.get("/api/nse")
def get_nse_data() -> List[Dict[str, Any]]:
    try:
        url = "https://afx.kwayisi.org/nse/"
        
        # Get the webpage content
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Read HTML tables
        tables = pd.read_html(response.text)
        
        # Get the 4th table (index 3)
        nse_df = tables[3]
        
        # Clean column names
        nse_df.columns = nse_df.columns.str.strip()
        
        # Convert numeric columns properly
        for col in nse_df.columns:
            if nse_df[col].dtype == 'object':
                # Try to convert to numeric, errors='ignore' keeps non-numeric as is
                nse_df[col] = pd.to_numeric(nse_df[col], errors='ignore')
        
        # Replace all NaN, inf, -inf with 0 for JSON compatibility
        nse_df = nse_df.replace([np.nan, np.inf, -np.inf, 'nan', 'NaN'], 0)
        
        # Additional cleaning: replace empty strings with 0
        nse_df = nse_df.replace('', 0)
        
        # Convert to records format
        records = nse_df.to_dict(orient="records")
        
        # Final safety check - ensure no problematic values remain
        clean_records = []
        for record in records:
            clean_record = {}
            for key, value in record.items():
                if pd.isna(value) or value is np.nan:
                    clean_record[key] = 0
                elif isinstance(value, float) and (np.isinf(value) or np.isnan(value)):
                    clean_record[key] = 0
                else:
                    clean_record[key] = value
            clean_records.append(clean_record)
        
        return clean_records
        
    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Failed to fetch data: {str(e)}")
    except IndexError:
        raise HTTPException(status_code=404, detail="Table not found on the webpage")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# For Vercel compatibility
handler = app