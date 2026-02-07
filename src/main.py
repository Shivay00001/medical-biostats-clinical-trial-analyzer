import argparse
import pandas as pd
from src.stats.engine import BiostatsEngine
from src.reporting.reporter import ClinicalReporter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Medical Biostats Clinical Trial Analyzer")
    parser.add_argument("--input", default="data/trial_data.csv", help="Input CSV data")
    parser.add_PH_argument("--output_report", default="output/summary.json", help="Output JSON report")
    parser.add_argument("--output_plot", default="output/survival_curve.png", help="Output PNG plot")

    args = parser.parse_args()

    try:
        logger.info(f"Loading trial data from {args.input}")
        df = pd.read_csv(args.input)
        
        # 1. Descriptive Stats
        logger.info("Calculating descriptive statistics")
        desc_stats = BiostatsEngine.descriptive_stats(df, "efficacy_score")
        
        # 2. T-Test
        logger.info("Running efficacy T-test")
        t_test_results = BiostatsEngine.run_t_test(df, "group", "efficacy_score")
        
        # 3. Survival Analysis
        logger.info("Running survival analysis")
        survival_results = BiostatsEngine.survival_analysis(df, "days", "event", "group")
        
        # 4. Generate Reports
        logger.info("Generating reports")
        final_results = {
            "descriptive": desc_stats,
            "efficacy_t_test": t_test_results,
            "survival": "Survival analysis completed"
        }
        
        ClinicalReporter.generate_summary(final_results, args.output_report)
        ClinicalReporter.plot_survival_curve(survival_results, args.output_plot)
        
        logger.info("Analysis successfully completed.")

    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        raise

if __name__ == "__main__":
    main()
