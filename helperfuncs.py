from datetime import datetime
from datetime import timedelta
import numpy as np
import scipy.stats as stats


def get_day_array(date_string = "2018-02-11", days = 9):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    dates = []
    for i in range(days):
        previous_date = date - timedelta(days=i+1)
        dates.append(previous_date.strftime("%Y-%m-%d")) 
    dates.reverse()
    return dates


def correlation_analysis(df):
    # Calculate the Pearson correlation coefficient and p-value
    corr_coef, p_value = stats.pearsonr(df.iloc[:, 0], df.iloc[:, 1])
    
    # Output the results
    print("Pearson correlation coefficient: {:.2f}".format(corr_coef))
    print("P-value: {:.4f}".format(p_value))


