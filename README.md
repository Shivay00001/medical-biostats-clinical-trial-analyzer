# Medical Biostats Clinical Trial Analyzer

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1-150458.svg)](https://pandas.pydata.org/)
[![Scipy](https://img.shields.io/badge/Scipy-1.11-8CAAE6.svg)](https://scipy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade biostatistical analysis platform** for clinical trials. Designed for pharmaceutical and medical research, this repository provides rigorous tools for analyzing trial efficacy, safety profiles, and patient survival rates using industry-standard statistical methodologies.

## 🚀 Features

- **Efficacy Analysis**: Automated t-tests, ANOVA, and regression modeling for clinical endpoints.
- **Survival Analysis**: Implementation of Kaplan-Meier estimators and Log-Rank tests.
- **Safety Reporting**: Automated generation of Adverse Event (AE) summaries and risk ratios.
- **Data Validation**: Strict CDISC-aligned data cleaning and validation pipelines.
- **Visual Analytics**: Professional-grade survival curves and forest plots.
- **Containerized**: Reproducible environment for regulatory-grade biostatistical reporting.

## 📁 Project Structure

```
medical-biostats-clinical-trial-analyzer/
├── src/
│   ├── stats/        # Statistical analysis logic
│   ├── reporting/    # Visualization and report generation
│   └── main.py       # Analysis entrypoint
├── data/             # Sample clinical trial datasets (CSV)
├── tests/            # Statistical validation tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/medical-biostats-clinical-trial-analyzer.git

# Install
pip install -r requirements.txt

# Run Analysis
python src/main.py --input data/trial_data.csv
```

## 📄 License

MIT License
