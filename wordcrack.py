import hashlib
from string import *
import time
from tqdm import tqdm
import sys, getopt

filename = "small.txt"
numbers = False
digits = 1
capitals = False
onlyfirst = False
vowels = False
symbols = False

def main(argv):
	global filename
	global numbers
	global digits
	global capitals
	global onlyfirst
	global vowels
	global symbols
	tocrack = [
    #['b62ab3b97a9c1fe4c6d69086c1f4a0fd', 'c09973d4a649edd8', 'student'],     #Minna
    ['1cd679dd4f628094551a5b14edf8e9b4', '488927b52bc8c780', 'aapeli'],      #Minna lars2392
    ['69a4aebda499da56a5ff4b9b97a8ef47', '4711c8357b673f77', 'aku'],         #Minna
    #['572844e03ffab36db74f5929bea05130', 'f6f647324a3bc245', 'anttoni'],     #Minna Jonne5
    ['b206227ab0668d878f1fce5048869ff3', 'd5734b3669148753', 'arja'],        #Minna
    #['71d6625256a67ed40f313f625fb3e964', '29596e90a0f53590', 'evie'],        #Minna 97acclaim
    #['4297c2bd63f4374d3ad0bf6e4e12ed9a', 'd9eb12205ca347b7', 'hunter'],      #Minna 
    #['6d3818c48e4f962fae6a604b66b4b1f5', '2ebba36fff917f30', 'ivana'],       #Minna estaBlish3
    ['f0e4e7f2b0d649e383a547b23251129c', '3b552a9879375233', 'janita'],      #Minna
    #['e324112919b8863fe2a5faccac133304', 'c09973d4a649edd8', 'janni'],       #Minna agrarian
    ['3777ae9f8421e2cec4d79bc130053bee', 'f7caacf6f546e8f7', 'jian'],        #Minna
    ['8e631babfdf4ce70d1ce4151ea891d08', 'aae79dea7fb83d4b', 'juhana'],      #Minna
    ['c1c3a88b9582d54cf9f6af71c5077304', '4a6b04c4531427dc', 'kingdom'],     #Minna
    ['167bef6988913ec485d0de423327a907', '8178c5cb2ea44340', 'kirsti'],      #Minna
    ['2c3746f1b626d32e6f63c4ba11b7328f', '3fc9d726d07fec58', 'lilly'],       #Minna
    ['f05f58daf8a4a5ed5b39ef47d135d4f7', '542284da2ab7cdc8', 'luz'],         #Minna
    ['186c28326f135e2971943b24a26fa016', '8662799239fe616d', 'marwa'],       #Minna
    ['fe7f8708cc8a58fe4f64748318b91418', 'be541cd6914ca7d2', 'mathis'],      #Minna
    ['c0d5bd820b93bcf6cc77644d89d53957', 'b3a0aaf319df3cc7', 'mirva'],       #Minna
    ['32d4563bf80740dc7aeef1fe8d04f5ad', '799ae722562befc6', 'paul'],        #Minna
    ['a54c640ae05eac55f6b0cef9b0062e44', '82b3e4914ad20565', 'peter'],       #Minna
    ['ac08617c835486efe2f63aa868efd783', '3ddba1ddab51be52', 'rebekka'],     #Minna
    ['f7723f7111ebb8939d5d84cb3b9e8ca8', 'c09973d4a649edd8', 'robo'],        #Minna
    #['a32ffc52e18395431fd0cbe061f319d5', '97439821263b5c85', 'ronja'],       #Minna Uphold
    ['7ac26bd732615bf7324f57444dbab0f2', 'bc8ceea6916e2f52', 'samuel'],      #Minna
    ['b579aeae5d042276b040b35e58e34c1e', '21f13a27069eb1eb', 'santino'],     #Minna
    ['5f8e5f93e280458616ad6a7b877225ab', 'c736b51a18c0eb64', 'sauli'],       #Minna
    ['5020e3f6a3a58f0dac81798b6c9d2846', '1c8f9c594e65a01f', 'siddhartha'],  #Minna
    ['8602f15793d6c9fd7126e86bdb9a3175', '4742a5345dcff239', 'suvi'],        #Minna
    ['43f987b1bf196a1e8e7ba0a0c490f4f1', '25068c201ae82505', 'teemu'],       #Minna
    ['fc606bc0a90cc2b9ee47948689137b50', '248a5361e4eff006', 'teura'],       #Minna
    #['b72c399863e06a214a336e45921d3feb', '7a39c28abf7f3ee9', 'ukko'],        #Minna guessable51
    ['90fb497bfb2392ae8597e29985de6a81', '9618b8c9ed8cee1c', 'vellamo'],     #Minna
    ['fb28a791c3046579a6dd94deb69b103c', 'd6e909b1aa6b8bde', 'vilppu']]       #Minna
	try:
		opts, args = getopt.getopt(argv, "hf:d:ncvas", ["help"])
	except getopt.GetoptError:
		print("wordcrack.py -f wordlist.txt")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print("'-f filename.txt' defines the wordlist to use" + 
			"\n'-n' add 1 number" +
			"  '-d 2' add 2 numbers" +
			"\n'-c' capitalize the first letter" +
			"  '-a' capitalize any letter" +
			"\n'-v' replace vowels with numbers and symbols" +
			"\n'-s' add a symbol") 
	
			sys.exit()
		elif opt == '-f': #file
			filename = arg
		elif opt == '-n': #numbers 
			numbers = True
			digits = 1
		elif opt == '-d': #digits
			numbers = True
			digits = int(arg)
		elif opt == '-c': #capitals
			capitals = True
			onlyfirst = True
		elif opt == '-a': #anycapital
			capitals = True
			onlyfirst = False
		elif opt == '-v': #vowels
			vowels = True
		elif opt == '-s': #symbols
			symbols = True
	print(	"\nFile:     " + str(filename) + 
	"\nNumbers:  " + str(numbersprint()) + 
	"\nCapitals: " + str(capitalsprint()) + 
	"\nVowels:   " + str(vowels) + 
	"\nSymbols:  " + str(symbols) + "\n")   		
	wordcrack(tocrack)

def capitalsprint():
	if capitals and onlyfirst:
		return "First Letter"
	elif capitals:
		return "Any Letter"
	else:
		return "False"

def numbersprint():
	if numbers:
		return digits
	else:
		return False

def countlines(filename):
	counter = 0
	wordlist = open(filename, "r")
	for word in wordlist:
		counter += 1
	wordlist.close()
	return counter

def wordcrack(tocrack): 
	listsize = countlines(filename)
	wordlist = open(filename, "r")
	for word in tqdm(wordlist, total=listsize, mininterval=0.5, unit=" words"):
		password = word.rstrip("\r\n").lower()
		if password == "":
			continue		
		for user in tocrack:		
			if makehash(password, user[1]) == user[0]:
				success(user[2], str(password))
		if numbers:
			addnumbers(tocrack, password)
		if capitals:
			capitalize(tocrack, password)
		if vowels:
			replacevowels(tocrack, password)
		if symbols:
			addsymbol(tocrack, password)		
	wordlist.close()
	print("Done.")

# NUMBERS
def addnumbers(tocrack, password):
	maxvalue = 10**int(digits)
	for i in range(maxvalue):
		pw = password + str(i)
		for user in tocrack:			
			if makehash(str(pw), user[1]) == user[0]:
				success(user[2], str(pw))
		if capitals:
			capitalize(tocrack, pw)
		if vowels:
			replacevowels(tocrack, pw)
		if symbols:
			addsymbol(tocrack, pw)

#SYMBOLS
def addsymbol(tocrack, password):
	for i in "!?&#":
		pw = password + i
		for user in tocrack:
			if makehash(str(pw), user[1]) == user[0]:
				success(user[2], str(pw))
		if capitals:
			capitalize(tocrack, pw)
		if vowels:
			replacevowels(tocrack, pw)
			
		
#CAPITALS
def capitalize(tocrack, password):
	if password == "":
		return	
	if onlyfirst:
		if password[0].islower() == False:
			return
		pw = password.capitalize()
		for user in tocrack:		
				if makehash(str(pw), user[1]) == user[0]:
					success(user[2], str(pw))
	else:
		for i in range(len(password)):
			if password[i].islower() == False:
				continue
			pw = capitalize_i(password, i)
			for user in tocrack:		
				if makehash(str(pw), user[1]) == user[0]:
					success(user[2], str(pw))		

def capitalize_i(password, i):
	return password[:i].lower() + password[i:].capitalize()



#VOWELS
def replacevowels(tocrack, password):
	vowels = "aeiouy"
	replacements = "1234567890!?&#"
	if password == "":
		return
	for i in range(len(password)):
		pwlist = list(password)
		if pwlist[i] in vowels:
			for value in replacements:
				pwlistcopy = pwlist
				pwlistcopy[i] = value
				pw = ''.join(pwlistcopy)
				for user in tocrack:
					if makehash(str(pw), user[1]) == user[0]:
						success(user[2], str(pw))
				if capitals:
					capitalize(tocrack, pw)

def makehash(word, salt):
	p = hashlib.sha256()
	pw = str("potPlantSalt") + str(word) + str(salt)
	try:
		p.update(pw.encode('utf-8'))
	except UnicodeDecodeError:
		pass
	truncatedhex = truncate(p.hexdigest())
	return truncatedhex   
    
def truncate(str):
    return str[:32]

def success(user, password):
	print(
	"\r--------------------------------------------------------------------------------" +
	"\nPassword found! User: " + user + " Password: " + password + 		"\n--------------------------------------------------------------------------------")
def test(tocrack):
	p = hashlib.sha256()
	print("testing student's pw")   
	truncatedhex = makehash("prVkG2JO", "59e14c8d72c88f74")
	if (truncatedhex == "6a9af8ed8c2cbbbc1c01f86881bde8e4"):
		print("found student's password to be: " + "prVkG2JO")
	else:
		print("bleh")
        
main(sys.argv[1:])
