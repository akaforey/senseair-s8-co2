# import time
import pandas as pd
from datetime import datetime, timedelta
from datetime import date

# import os


def get_table(hours=6):
	today = date.today()
	filename_today = f"co2_captures/{today}_co2.csv"
	yesterday = today - timedelta(days=1)
	filename_yesterday = f"co2_captures/{yesterday}_co2.csv"

#	print(filename_today, filename_yesterday)


	df = pd.concat([pd.read_csv(filename_yesterday, header=None), pd.read_csv(filename_today, header=None)], axis=0, ignore_index=True)
	df.columns = ['timestamp', 'co2']
	df['datetime'] = pd.to_datetime(df['timestamp'], utc=None, unit='s')
	
	# TODO filter based on hours parameter
	
#	print(df)
	table = df.loc[:, ['datetime', 'co2']].to_html(header="true")
	return table
