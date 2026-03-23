# Decision-Aware Validation Layer Prototype

This prototype demonstrates a minimal **Decision-Aware Validation Layer (DAVL)**.

## Features
- Validate data based on decision-specific requirements
- Compute decision fitness scores
- Suggest actions (fallback, warning, OK)
- Interactive Streamlit interface

## Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `streamlit run app.py`
3. Select a decision, see validation, scores, and recommended actions

## Notes
- Uses CSVs in `data_samples/`
- Extendable with ML-based anomaly detection or real-time pipelines
