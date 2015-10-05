# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string 
# (i.e. n will be in the range 0..len(str)-1 inclusive). 

# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
	s = ''
	for i, c in enumerate(str):
		if i != n:
			s += c
	return s

def missing_char_2(str, n):
   c = str[n]
   rstr = str.replace(c, '', 1)
   if rstr != str: return rstr
   return str  