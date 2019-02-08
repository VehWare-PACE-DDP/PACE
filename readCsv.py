import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import math
import matplotlib.pyplot as plt
import csv






def main():

	dfBlock = pd.read_csv("Block_Log.csv", encoding='utf-8')

	dfEye = pd.read_csv("Cursor_Log.csv", encoding='utf-8')



	plt.scatter(dfEye.loc[:, 'Time'], dfEye.loc[:, 'Bool'], marker='^',label='Test Results')
	plt.xlabel = 'Time'
	plt.ylabel = 'Accuracy'

	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.06),  shadow=True)

	plt.show()




if __name__ == '__main__':
	
	main()
