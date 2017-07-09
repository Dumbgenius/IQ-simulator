import argparse

import numpy as np
import matplotlib.pyplot as plt

def produceChild (iq1, iq2) :
	average = np.mean([iq1, iq2])
	child = np.random.normal(average, 10)
	return child;
	

if __name__ == "__main__" :
	parser = argparse.ArgumentParser()
	parser.add_argument("--people", "-p", dest="people", default=1000, type=int, help="Starting number of people")
	parser.add_argument("--iterations", "-i", dest="iterations", default=10, type=int, help="Iterations to run")
	options = parser.parse_args()
	
	numPeople = options.people
	maxIterations = options.iterations
	
	print("Starting population: %d. Maximum iterations: %d." % (numPeople, maxIterations))
	
	
	iq_arr = np.random.normal(100, 15, numPeople) #each item in the list is the person's IQ
	
	plt.subplot(211)
	plt.hist(iq_arr, 100)
	plt.xlabel("IQ")
	plt.ylabel("Frequency density")
	
#	print(iq_arr)
	
	for x in range(maxIterations):
		prev_iq_arr = np.array(iq_arr)
		iq_arr = []
		#np.random.shuffle(iq_arr)
		
		for y in range(numPeople):
			if prev_iq_arr[y] == 10000000000: #100000000 is an arbitrarily high placeholder
#				print ("Person #%03d already mated" % y)
				continue #skip this person
			else:
				shuffled = np.column_stack( (prev_iq_arr, np.arange(numPeople)) )
				np.random.shuffle(shuffled)
				
				mateID = np.nan #probably unnecessary, but it means we'll get an error if it somehow gets used as the index
				
				for z in range(numPeople):
					iq = shuffled[z][0]
					if iq == 10000000000: 
						continue
					
					if iq-20 < prev_iq_arr[y] and prev_iq_arr[y] < 20+iq:
						if y != int(shuffled[z][1]): #a person cannot mate with themselves!
							mateID = int(shuffled[z][1]) #the true ID of the first in the array that has IQ in the desired range
							break
				
				else:
#					print("Person #%03d (IQ %03d) did not find a mate! ------------------------------------!!" %(y, prev_iq_arr[y]))
					continue #skip this person, maybe someone will find them as a mate [although probably not, I think the above search is exhaustive]
					
#				print("Person #%03d (IQ %03d) mated with person %03d (IQ %03d)." %(y, prev_iq_arr[y], mateID, prev_iq_arr[mateID]))
				
				iq_arr.append( produceChild( prev_iq_arr[y], prev_iq_arr[mateID] ) )
				iq_arr.append( produceChild( prev_iq_arr[y], prev_iq_arr[mateID] ) ) # 2 children per set of parents
				
				
				prev_iq_arr[y] = 10000000000 #so they don't get selected again
				prev_iq_arr[mateID] = 10000000000
		
			#if y%500 == 0: print("Done %d." % y)
		
		print("------")
		print("Iteration #%d done." % (x+1))
		print("Current population: %d. %d died without a mate." % (len(iq_arr), numPeople-len(iq_arr)))
		numPeople = len(iq_arr)
	
	iq_arr.sort()
	
	# plt.subplot(211)
	# plt.plot(iq_arr)
	# plt.xlabel("Number of people (cumulative)")
	# plt.ylabel("IQ")

	plt.subplot(212)
	plt.hist(iq_arr, 100)
	plt.xlabel("IQ")
	plt.ylabel("Frequency density")

	plt.show()





