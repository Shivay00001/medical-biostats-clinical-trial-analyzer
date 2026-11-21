# Medical Biostats Clinical Trial Analyzer

Built by [VisionQuantech](https://visionquantech.com) — AI agents, apps & tools for small businesses.

An enterprise-grade solution engineered for high performance.

![Language](https://img.shields.io/badge/Language-Python-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-VisionQuantech%20Custom-orange)

## 🚀 Overview

Welcome to the **Medical Biostats Clinical Trial Analyzer** repository. This project is built to deliver a robust and scalable solution tailored to modern development standards.

This tool performs statistical analysis on clinical trial data (CSV format), computing descriptive statistics, independent two-group t-tests on efficacy scores, and Kaplan-Meier survival analysis — outputting a JSON summary report and a survival curve plot.

## ✨ Features

- **High Performance:** Optimized for speed and efficiency.
- **Scalable Architecture:** Designed to grow with your needs.
- **Clean Codebase:** Follows best practices and industry standards.
- **Secure by Default:** Engineered with security in mind.
- **Descriptive Statistics:** Summary statistics (count, mean, std, quartiles) for efficacy scores via `pandas`.
- **Independent T-Test:** Two-group efficacy comparison using `scipy.stats.ttest_ind`.
- **Survival Analysis:** Kaplan-Meier survival curves per treatment group using `lifelines`.
- **Automated Reporting:** JSON summary reports and publication-style survival plots (`matplotlib`/`seaborn`).
- **Containerized:** Fully Dockerized for reproducible, one-command execution anywhere.

## 🏗️ Architecture / How It Works

The pipeline is a linear, CLI-driven workflow:

```
data/trial_data.csv
        │
        ▼
┌─────────────────────┐
│   src/main.py       │  CLI entrypoint (argparse: --input, --output_report, --output_plot)
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│ BiostatsEngine      │  src/stats/engine.py
│  ├─ descriptive_stats()   → pandas .describe()
│  ├─ run_t_test()          → scipy ttest_ind (requires exactly 2 groups)
│  └─ survival_analysis()   → lifelines KaplanMeierFitter per group
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│ ClinicalReporter    │  src/reporting/reporter.py
│  ├─ generate_summary()    → output/summary.json
│  └─ plot_survival_curve() → output/survival_curve.png
└─────────────────────┘
```

**Input data schema** (`data/trial_data.csv`):

| Column | Description |
|---|---|
| `patient_id` | Unique patient identifier |
| `group` | Cohort label (e.g., `Treatment` / `Placebo`) — must be exactly 2 groups for the t-test |
| `efficacy_score` | Continuous efficacy measurement |
| `days` | Follow-up duration (survival time) |
| `event` | Event indicator (1 = event occurred, 0 = censored) |

> **Note:** The repository also contains a `main.go` / `go.mod` stub (a minimal HTTP health server on `:8080`). It is **not** wired into the analysis pipeline or the Docker image and appears to be scaffolding for a future service layer.

## 🛠️ Prerequisites

Ensure you have the following installed in your environment before proceeding:
- Python 3.11+ (or Docker — see below)
- Standard development tools

## 📦 Installation

Follow standard installation steps for `Python` to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Shivay00001/medical-biostats-clinical-trial-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd medical-biostats-clinical-trial-analyzer
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the analyzer against the bundled sample dataset:

```bash
python src/main.py \
  --input data/trial_data.csv \
  --output_report output/summary.json \
  --output_plot output/survival_curve.png
```

Results are written to `output/summary.json` (descriptive stats + t-test results) and `output/survival_curve.png` (Kaplan-Meier curves per group).

## 🐳 Running with Docker (Recommended)

The project ships with a `Dockerfile` and `docker-compose.yml` for fully reproducible, dependency-free execution on any laptop or server.

**Option 1 — Docker Compose (easiest):**
```bash
docker-compose up --build
```
This builds the image, runs the analysis against `data/trial_data.csv`, and writes results to the local `./output/` directory (mounted as a volume).

**Option 2 — Plain Docker:**
```bash
# Build the image
docker build -t biostats-analyzer .

# Run the analysis (mount ./output so results persist on your host)
docker run --rm -v "$(pwd)/output:/app/output" biostats-analyzer \
  --input data/trial_data.csv
```

To analyze your own dataset, mount it into the container:
```bash
docker run --rm \
  -v "$(pwd)/output:/app/output" \
  -v "$(pwd)/my_data.csv:/app/data/my_data.csv" \
  biostats-analyzer --input data/my_data.csv
```

## ⚠️ Workability Assessment

An honest evaluation of the current state of this repository:

**Verdict: NOT runnable as-is — requires a small but critical fix before use.**

- 🔴 **Blocking bug:** `src/main.py` calls `parser.add_PH_argument("--output_report", ...)`. `add_PH_argument` does not exist on `argparse.ArgumentParser` — this will raise an `AttributeError` immediately on startup. It must be changed to `add_argument`. **No execution path works until this is fixed.**
- 🟡 **Fragile plotting logic:** `ClinicalReporter.plot_survival_curve` assumes each group's survival dictionary values are dicts keyed by group label (`v[label]`), which matches the current engine output but is brittle — any change to the engine's return shape (e.g., a flat `{time: probability}` dict) will silently break plotting.
- 🟡 **Potential crash on empty output dir:** `generate_summary` calls `os.makedirs(os.path.dirname(output_path))`, which fails if `output_path` has no directory component (e.g., `"summary.json"`).
- 🟡 **No tests:** `pytest` is listed in `requirements.txt` but no test files exist in the repository.
- 🟡 **Dead/confusing code:** The Go `main.go` HTTP server is unrelated to the Python analyzer, unreferenced by Docker, and may confuse contributors. The README badge previously claimed an MIT license, but the actual `LICENSE` is the VisionQuantech Custom Commercial License.
- 🟡 **Statistical limitations:** The t-test assumes exactly two groups and does not check assumptions (normality, equal variance); there is no log-rank test to compare survival curves, no confidence intervals on KM curves, and no handling of missing data.
- 🟢 **Positives:** Clean module separation (`stats` / `reporting`), sensible dependency choices (`lifelines`, `scipy`, `pandas`), a working Docker setup, and a correct Kaplan-Meier implementation for the bundled sample data.

**Bottom line:** With the one-line `add_PH_argument` → `add_argument` fix, the tool will run end-to-end on the sample data and produce correct outputs. It is a solid prototype/learning-grade tool, but it is **not production-ready** for real clinical analysis without tests, input validation, additional statistical rigor (log-rank tests, CIs), and code cleanup.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page. High-value contributions include: fixing the CLI bug, adding a pytest suite, adding a log-rank test, and input validation.

## 📝 License

This project is licensed under the **VisionQuantech Custom Commercial License** — see the [LICENSE](LICENSE) file for full terms. In summary:

- **Personal / educational / non-earning use:** Free.
- **Individual revenue-generating use:** Requires a 15–30% revenue share.
- **Business / enterprise use:** Requires a separate commercial license — contact **visionquantech@proton.me**.