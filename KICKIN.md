# Project Kick-in Guide

Welcome to the Telecom Churn Prediction project! This document is a quick start guide to help you get the project up and running in no time.

---

## Environment Setup

1. Make sure you have Python 3.8+ installed on your system.
2. Create a new virtual environment to keep dependencies isolated:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

---

## Install Dependencies

Run the following command to install all required packages:

```
pip install -r requirements.txt
```

---

## Running the Project

### To start the Flask API server:
```
python src/api/main.py
```

### To launch the interactive Streamlit dashboard:
```
streamlit run src/churn_predictor/streamlit_dashboard.py
```

---

## Project Structure Overview

- `data/raw/` – Original datasets
- `models/` – Saved machine learning models
- `src/api/` – API backend code
- `src/churn_predictor/` – ML pipeline and dashboards
- `screenshots/` – Project screenshots for documentation and reports
- `notebooks/` – Jupyter notebooks for documentation and experimentation
- `reports/` – Business reports and analysis

---

## Helpful Tips

- Always activate the virtual environment before running scripts.
- Use `git pull` regularly to keep your local copy updated.
- Check `/tests/` folder for any automated tests you can run.

---

## Contact & Support

If you run into any issues or have questions, reach out to:

**Karan Sharma**  
📧 karanku1882@gmail.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/karan-sharma-167957271)

---

*Happy Coding & Best of Luck!*

***
