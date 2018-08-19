'''
Naive solution: check every pairs of char -> O(n^2)
'''
def first_recurring(given_string):
	counts = {}
	for c in given_string:		
		if c in counts:			
			print c
			return c	
		counts[c]=1

if __name__=='__main__':	
	first_recurring('avcbhbht')