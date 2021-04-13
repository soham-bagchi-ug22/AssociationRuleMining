import csv
import collections
import math
from tabulate import tabulate

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
	n = 1
	while(1 != 0):
		tempR = []
		tempL = []
		for i in range(len(R[n])):
			for j in range(len(R[1])):
				if(checkExists(R[1][j], R[n][i]) == False): # Fix this to work with lists
					New = intersection(L[n][i], L[1][j])
					if(len(New) >=k):
						if(n == 1):
							tempR.append([R[n][i], R[1][j]])
						else:
							tempR.append( R[n][i] + [ R[1][j] ] )
						tempL.append(New)
		if(len(tempR)==0):
			return
		R.append(tempR)
		L.append(tempL)
		R[n+1], L[n+1] = checkDuplicates(R[n+1], L[n+1])		
		print("\nLevel ", n+1, "-->  Length = ", len(R[n+1]))
		print(R[n+1])
		print("\n")
		n+=1


def printList(R, L, T, k):
	tempR = []
	tempL = []
	for i in range(len(R[0])):
		if(len(L[0][i]) >= k):
			tempR.append(R[0][i])
			tempL.append(L[0][i])
	R.append(tempR)
	L.append(tempL)
			
	print("For k = ", k)
	print("Level 1  -->  Length = ", len(R[1]))
	print(R[1])
	print("\n")
	
	getLevels(R, L, k)
	

def associationSearch(R, L, s):
	n = len(s)
	#check if s exists in level n frequent itemset
	#if it exists, record the length of the transaction id's that itemset has <=> CHECK EXISTS
	query = []
	queryIsFrequent = False
	queryTransactionCount = 0
	if(n == 1):
		for i in range(len(R[n])):
			if(s[0] == R[n][i]):
				query = [R[n][i]]
				queryIsFrequent = True
				queryTransactionCount = len(L[n][i])
				break
	else:
		for i in range(len(R[n])):
			if(compareLists(s, R[n][i])):
				query = R[n][i]
				queryIsFrequent = True
				queryTransactionCount = len(L[n][i])
				break
		
	if(queryIsFrequent == False):
		print(s, "not found in frequent itemsets.")
		return
	
	print(query)
	print(queryTransactionCount) # Number of baskets where you find s
	
	confidenceCount = []
	#move up to the next level n+1	
	for i in range(len(R[n+1])):
		#check if s exists in that level, if it does't, print no associated item found
		if(all(item in R[n+1][i] for item in query)):
			#find all itemsets that have s
			#record the length of the transaction id's that these itemsets have, calculate confidence
			temp = "%.2f" % (len(L[n+1][i])*100/queryTransactionCount)
			confidenceCount.append([R[n+1][i], temp])
	if(len(confidenceCount)==0):
		print("No associated items found.")
		return
	
	#print(confidenceCount)
	print(tabulate(confidenceCount, headers=['Itemsets', 'Confidence']))
""" 
def generateAssociationData(R, L):
	allAssociationData = []
	for i in range(len(R)):
		associationData
		for j in range(len(R[i])):
 """

def main():
	A = importCSV('groceries.csv')
	
	k = float(input("Enter Support Percentage: "))
	k = math.floor(k*len(A)/100) #k input is in percentage for the business minded ducks


	# S              ,,, ::::::::::::..
	# O          ,z$$$$$ :::::::::::::::::.
	# H        e$$$$$$$$ ::::::::::::::::::::
	# A      d$$$$$$$$$$;`::::::::::::::::::::
	# M     ::."$$$$$$$$$ :::::::::::::::::::::
	#      :::::."$$$$$$$ ::::::::::::::::::::
	#     ::::::::."$$$$$b ::''''''''':::::::'
	#     `:::::::::`$$P" . :''''<<<<<<;.  `'
	#       `:::::::: "".,.----=--..`'<<<<<<;
	#         `:::'',-'` .::::::::::`'- `<<<<;      .::.
	#           `,-`.::::::::::'  .. `::.      .:::::::::
	#         ,-'.:::::::::::' dMMMMMMx :::::` .`::::::::
	#       ,'.::::::::::::: dMMMMMMMMMM ``` JMMM `:::::
	# N   ,'.:::::::::::' . MMP',ccc "MMM Mb MMMMM `:::
	# E  ; :::::::::::' nM MM',$$$$$$b "Mb4M,M c,`? :'
	# I ; ::::::::::: xMMMMM'J$$$$$$$$b )MMMMM.`$$.
	# L' :::`::::::: dMMMMM'J$$$$$$$$$$F MMMMMM $$$.
	#    :: <`::::: JMMMMM',$$$$$$$$$$$P MMMMMM $$$$
	#   `:::`bc,.. ,edMMMM $$$$$$$$$$$$F MMMMMM $$$$  .
	#    ` ,nMMMMMMMMTMMMM P""?$$$$$$$$".MTT4MM ?$$F;P""?x_
	#    ,d)MMMMMMP'dMMMMM      $$$$$$P  .cCc.    $   cCc L~
	#     ,MMMMMMM ,c, 4MMr      $$$$$  .CCCC>   4   CCC> L"
	# S   P)MMMMM> $$?$ "MM      $$$$"  CCCCC'   ,,  CC> % `
	# I  ' MMMTMMM `b $$c.?b     $$$"   `CCC'-""___,,,,,__
	# D    M"       `?, ??$c,,,,,,cc$7= _,cc$$$$PP"""""??$$$$
	# D    "          `"b,_ "?$$$$$$$$$$P""'.. ,d"
	# H                  `?$b `,,,,,,.`;;;;;;'j"
	# A                   n ?$c`;;;;;;;`',;;; F
	# R              ,;- ;MM "$b ;;;;;,,;;;'j"
	# T          ,!!!!!  MMMM,`?$c,_`` _,,cd'
	# H         !!!!!!!; MMMMMMn, `"""""''
	# A      .  !!!!!!!!!, `"TT';!!!!>
	#    ,;!!!> !!!!!!!!!!!!!   ` !!!!!!;;

	N = findUniqueItems(A)
	T = createTransactionFrequency(N, A)

	R = []
	R.append(N) #first element of R holds all the unique items
	L = []
	L.append(T)#First element of L holds the TID's associated with each unique item
	printList(R,L,T,k)
	
	s = ['whole milk']
	associationSearch(R, L, s)

	
main()
