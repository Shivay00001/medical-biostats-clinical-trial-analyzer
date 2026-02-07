import matplotlib.pyplot as plt
import seaborn as sns
import os

class ClinicalReporter:
    @staticmethod
    def plot_survival_curve(survival_data, output_path):
        """Generates and saves survival curves."""
        plt.figure(figsize=(10, 6))
        for label, data in survival_data.items():
            times = list(data.keys())
            probs = [v[label] for v in data.values()]
            plt.step(times, probs, label=label)
            
        plt.title("Kaplan-Meier Survival Curves")
        plt.xlabel("Days")
        plt.ylabel("Survival Probability")
        plt.legend()
        plt.grid(True)
        plt.savefig(output_path)
        plt.close()

    @staticmethod
    def generate_summary(results, output_path):
        """Saves analysis results to a JSON file."""
        import json
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=4)
