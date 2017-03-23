"""
This code generates lexical categories for the text provided in the CSV files.
First columns can be any data, be sure to find a title for each row in Line 16!
The last column will be analysed
As a delimiter choose ";" (MS Excel standard)

For further information check the GitHub project:
https://github.com/Ejhfast/empath-client
"""
import csv
from empath import Empath

lexicon = Empath()
#new categories could be created here
#generate titlerow
titlerow = ['worker ID','Code','comment']


#Settings
normalisation = False
input_filename = 'maxqda_experiment'
output_filename = 'maxqda_output'
number_of_files = 2
seperator = ';' #MS Excel Standard
data_cols = len(titlerow)
#extend with categories
titlerow.extend(sorted(lexicon.cats.keys()))

#run for the number of input files
for i in [1,number_of_files]:
	print ('reading file %d' % i)
	file = open('%s%d.csv' % (input_filename, i) , 'r')
	#convert csv to list, excel uses ";" as delimiter 
	list = list(csv.reader(file, delimiter=seperator, lineterminator='\n'))
	file.close()
	
	#iterate over the given list and update numbers after analysing
	print('analysing file %d' % i)
	for row in list:
		#analysing returns a dictionary of categories and a matching number
		categories = lexicon.analyze(row[data_cols-1], normalize=normalisation)
		#get values of the dict and store them in the list
		for cat in range(3,len(categories)+3):
			row.append(categories[titlerow[cat]])
	print('writing output file %d' % i)
	csv_writer = csv.writer(open('%s%d.csv' % (output_filename, i),'w'),delimiter=seperator,lineterminator='\n')
	i =csv_writer.writerow(titlerow)
	for row in list:
		csv_writer.writerow(row)
	#make space for next run
	del list
print ('Done!')