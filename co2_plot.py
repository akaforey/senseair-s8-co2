import pandas as pd
from datetime import timedelta, date
from matplotlib import pyplot as plt
import os


def plot(hours=6):
	today = date.today()
	filename_today = f"co2_captures/{today}_co2.csv"
	yesterday = today - timedelta(days=1)
	filename_yesterday = f"co2_captures/{yesterday}_co2.csv"

	df = pd.concat([pd.read_csv(filename_yesterday, header=None), pd.read_csv(filename_today, header=None)], axis=0, ignore_index=True)
	df.columns = ['timestamp', 'co2']
	
	# TODO filter based on hours parameter

	df.plot(x='timestamp', y='co2')
	output_location = os.path.join(os.getcwd(), 'figures', 'co2_plot.png')
	plt.savefig(output_location)
	
	return output_location


if __name__ == "__main__":
	plot()
