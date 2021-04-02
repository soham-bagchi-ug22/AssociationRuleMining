import csv
import collections
import math

def importCSV(file):
	with open(file, 'r') as groceries_obj:
		groceries_csv = csv.reader(groceries_obj)
		list_of_rows = list(groceries_csv)
		return list_of_rows

def checkExists(item, dictionary):
	if(item in dictionary):
		return True
	return False

def findUniqueItems(A):
	B = []
	for i in range(len(A)):
		for j in range(len(A[i])):
			if(checkExists(A[i][j], B) == False):
				B.append(A[i][j])
	return B

def createTransactionFrequency(uniqueItems, transactionList):
	T = [[] for i in range(len(uniqueItems))]
	for i in range(len(uniqueItems)):
		tList_ = []
		for j in range(len(transactionList)):
			if(checkExists(uniqueItems[i], transactionList[j])):
				tList_.append(j)
		T[i] = tList_
	return T

def intersection(lst1, lst2):
    # Use of hybrid method
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


def compareLists(L1, L2):
	return(collections.Counter(L1) == collections.Counter(L2))


def checkDuplicates(P, T):
	listOfJays = [] #initialize empty array to hold indices for all itemsets that are the same
	for i in range(len(T)):
		for j in range(i+1, len(T)):
			if(T[i] == T[j]):
				if(compareLists(P[i],P[j])):
					listOfJays.append(j)
	for i in range(len(listOfJays)):
		P[listOfJays[i]] = 0
		T[listOfJays[i]] = 1
		
	x = len(T)-1
	i = 0
	newP = []
	newT = []
	for i in range(len(P)):
		if(P[i] != 0):
			newP.append(P[i])
			newT.append(T[i])
	return newP, newT

						
def getLevels(R,L,k):
	for n in range(1,len(R)-1):
		for i in range(len(R[n])):
			for j in range(len(R[1])):
				if(checkExists(R[1][j], R[n][i]) == False): # Fix this to work with lists
					New = intersection(L[n][i], L[1][j])
					if(len(New) >=k):
						if(n == 1):
							R[n+1].append([R[n][i], R[1][j]])
						else:
							R[n+1].append( R[n][i] + [ R[1][j] ] )
						L[n+1].append(New)
		R[n+1], L[n+1] = checkDuplicates(R[n+1], L[n+1])		
		print("Level ", n+1, "-->  Length = ", len(R[n+1]))
		print(R[n+1])
		#print(L[n+1])
		print("\n")


def printList(R, L, T, k):
	temp = []
	for i in range(len(R[0])):
		if(len(L[0][i]) >= k):
			R[1].append(R[0][i])
			L[1].append(L[0][i])
			
			
	print("For k = ", k)
	print("Level 1  -->  Length = ", len(R[1]))
	#print(R[1])
	#print(L[1])
	print("\n")
	
	getLevels(R, L, k)
	

def main():
	A = importCSV('groceries.csv')
	
	k = int(input("Enter Support Percentage: "))
	k = math.floor(k*len(A)/100)


	# 										.;;;..
	# 									;<!!!!!!!!;
	# 								.;!!!!!!!!!!!!>
	# 							.<!!!!!!!!!!!!!!!
	# 							;!!!!!!!!!!!!!!!!'
	# 							;!!!!!!!!!!!!!!!!!'
	# 						;!!!!!!!!!!!!!!!''
	# 						,!!!!!!!!!!!!!'` .::
	# 				,;!',;!!!!!!!!!!!'` .::::''  .,,,,.
	# 				!!!!!!!!!!!!!!!'`.::::' .,ndMMMMMMM,
	# 				!!!!!!!!!!!!!' .::'' .,nMMP""',nn,`"MMbmnmn,.
	# 				`!!!!!!!!!!` :'' ,unMMMM" xdMMMMMMMx`MMn
	# 			_/  `'!!!!''`  ',udMMMMMM" nMMMMM??MMMM )MMMnur=
	# ,.... ......--~   ,       ,nMMMMMMMMMMnMMP".,ccc, "M MMMMP' ,,
	# `--......--   _.'        " MMP??4MMMMMP ,c$$$$$$$ ).MMMMnmMMM
	# 	_.-' _..-~            =".,nmnMMMM .d$$$$$$$$$L MMMMMMMMMP
	# .--~_.--~                  '.`"4MMMM  $$$$$$$$$$$',MMMMMPPMM
	# `~~~~                      ,$$$h.`MM   `?$$$$$$$$P dMMMP , P
	# 						<$""?$ `"     $$$$$$$$',MMMP c$
	# 						`$c c$h       $$$$$$$',MMMM  $$
	# 							$$ $$$       $$$$$$',MMMMM  `?
	# 							`$.`$$$c.   z$???"  "',,`"
	# 							3h $$$$$cccccccccc$$$$$$$$$$$=r
	# 							`$c`$$$$$$$$$$$$$$$??$$$$F"$$ "
	# 						,mr`$c`$$$$$$$$$$$$$$c 3$$$$c$$
	# 						,mMMMM."$.`?$$$$$$$$$$$$$$$$$$$$$$h,
	# ;.   .               .uMMMMMMMM "$c,`"$$$$$$$$$$$$$$$$C,,,,cccccc,,..
	# !!;,;!!!!> .,,...  ,nMMMMMMMMMMM.`?$c  `"?$$$$$$$$$$$$$$$$$$$$$$$$$$$$h.
	# !!!!!!!!! uMM" <!!',dMMMMMMMMMMPP" ?$h.`::..`""???????""'..  -==cc,"?$$P
	# !!!!!!!!'.MMP <!',nMMMMMMMMP" .;    `$$c,`'::::::::::::'.$F
	# !!!!!!!! JMP ;! JMMMMMMMP" .;!!'      "?$hc,.````````'.,$$
	# !!!!'''' 4M(;',dMMMP""" ,!!!!` ;;!!;.   "?$$$$$?????????"
	# !!! ::. 4b ,MM" .::: !''`` <!!!!!!!!;
	# `!::::.`' 4M':::::'',mdP <!!!!!!!!!!!;
	# ! :::::: ..  :::::: ""'' <!!!!!!!!!!!!!!;
	# !! ::::::.::: .::::: ;!!> <!!!!!!!!!!!!!!!!!;.
	# !! :::::: `:'::::::!!' <!!!!!!!!!!!!!!!!!!!!!;;.
	# ! ::::::' .::::' ;!' .!!!!!!!!!!!!!!'`!!!!!!!!!!!;.
	# ; `::';!>  ::' ;<!.;!!!!!!!''''!!!!' <!! !!!!!!!!!!!>

	# ------------------------------------------------
	# Thank you for visiting https://asciiart.website/
	# This ASCII pic can be found at
	# https://asciiart.website/index.php?art=animals/birds%20(water)

	N = findUniqueItems(A)
	T = createTransactionFrequency(N, A)

	R = [[] for i in range(6)]
	R[0] = N #first element of R holds all the unique items

	L = [[] for i in range(6)]
	L[0] = T #First element of L holds the TID's associated with each unique item
	printList(R,L,T,k)

main()

def associationSearch(R, L, s):
	n = len(s)
	#check if s exists in level n frequent itemset
	#if it exists, record the length of the transaction id's that itemset has <=> CHECK EXISTS
	query = []
	queryIsFrequent = False
	queryTransactionCount = 0
	for i in range(len(R[n])):
		if(compareLists(s, R[n][i])):
			query = R[n][i]
			queryIsFrequent = True
			queryTransactionCount = len(L[n][i])
			break

	confidenceCount = []
	#move up to the next level n+1	
	for i in range(len(R[n+1])):
		#check if s exists in that level, if it does't, print no associated item found
		if(all(item in R[n+1][i] for item in query)):
			#find all itemsets that have s
			#record the length of the transaction id's that these itemsets have, calculate confidence
			confidenceCount.append([R[n+1][i], len(L[n+1][i])/queryTransactionCount])

	print(confidenceCount)	
