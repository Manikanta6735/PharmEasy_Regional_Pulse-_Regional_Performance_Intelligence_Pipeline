# PharmEasy Regional Pulse — Regional Performance Intelligence Pipeline

## Setup & Run Instructions

To install dependencies and run the entire pipeline end-to-end from a fresh clone, execute the following three commands in your terminal:

```bash
pip install pandas streamlit plotly
python3 generate_dataset.py && python3 clean_data.py && python3 build_db.py
streamlit run app.py"# PharmEasy_Regional_Pulse-_Regional_Performance_Intelligence_Pipeline" 
