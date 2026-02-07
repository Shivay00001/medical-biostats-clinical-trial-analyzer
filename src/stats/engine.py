import pandas as pd
import numpy as np
from scipy import stats
from lifelines import KaplanMeierFitter

class BiostatsEngine:
    @staticmethod
    def run_t_test(data, group_col, value_col):
        """Performs an independent t-test between two groups."""
        groups = data[group_col].unique()
        if len(groups) != 2:
            raise ValueError("T-test requires exactly two groups.")
        
        group1 = data[data[group_col] == groups[0]][value_col]
        group2 = data[data[group_col] == groups[1]][value_col]
        
        t_stat, p_val = stats.ttest_ind(group1, group2)
        return {"t_statistic": t_stat, "p_value": p_val}

    @staticmethod
    def survival_analysis(data, duration_col, event_col, group_col):
        """Performs Kaplan-Meier survival analysis."""
        kmf = KaplanMeierFitter()
        results = {}
        
        for group in data[group_col].unique():
            mask = (data[group_col] == group)
            kmf.fit(data[duration_col][mask], event_observed=data[event_col][mask], label=group)
            results[group] = kmf.survival_function_.to_dict()
            
        return results

    @staticmethod
    def descriptive_stats(data, value_col):
        """Returns basic descriptive statistics."""
        return data[value_col].describe().to_dict()
