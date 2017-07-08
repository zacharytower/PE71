from fractions import Fraction

def sorted_fractions(n):
	'''
	prints out a list of sorted fractions for all d <= n
	'''

	fraction_set = set()
	for denominator in range(2, n + 1): # for all denominators <= n:
		#print denominator 
		for numerator in range(1, denominator): # for all numerators < denominator:
			
			frac = Fraction(numerator, denominator)
			if frac not in fraction_set:
				fraction_set.add(frac)

	sorted_fraction_list = sorted(list(fraction_set))

	return sorted_fraction_list

def sorted_fraction_list_len(n):
	return len(sorted_fractions(n))



def main(a):

	n = a # n is upper limit for d.

	fraction_set = set()

	for denominator in range(2, n + 1): # for all denominators <= n:
		#print denominator 
		for numerator in range(1, denominator): # for all numerators < denominator:
			
			frac = Fraction(numerator, denominator)

			if frac > Fraction(3,7):
				break

			if frac not in fraction_set:
				fraction_set.add(frac)

			#previous_frac = frac

	sorted_fraction_list = sorted(list(fraction_set))

	return sorted_fraction_list[-2]

if __name__ == '__main__':
	'''
	for a in range(4,400):

		print a,main(a)'''

	for i,f in enumerate(sorted_fractions(256)):
		print i+1, f
