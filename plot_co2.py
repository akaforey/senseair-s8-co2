import time
import pandas as pd
from datetime import datetime, timedelta
from datetime import date
from matplotlib import pyplot as plt
import os


def plot_co2(hours=6, location="static"):
	today = date.today()
	filename_today = f"co2_captures/{today}_co2.csv"
	yesterday = today - timedelta(days=1)
	filename_yesterday = f"co2_captures/{yesterday}_co2.csv"

#	print(filename_today, filename_yesterday)


	df = pd.concat([pd.read_csv(filename_yesterday, header=None), pd.read_csv(filename_today, header=None)], axis=0, ignore_index=True)
	df.columns = ['timestamp', 'co2']
	df['datetime'] = pd.to_datetime(df['timestamp'], utc=True, unit='s').map(lambda x: x.tz_convert('America/New_York'))
	
	# TODO filter based on hours parameter
	
#	print(df)
	df.plot(x='datetime', y='co2')
#	plt.show
	output_location = os.path.join(os.getcwd(), location, 'co2_plot.png')
	plt.savefig(output_location)
	
	return output_location

if __name__ == "__main__":
	plot_co2()
