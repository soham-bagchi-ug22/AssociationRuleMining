import csv
import collections

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:07:59 2021

@author: ashuc
"""
#N = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#T = [[1,3,4], [1,2,3,5], [2,3,4], [1,2,5], [2,4,5], [1,3,4,5], [2,4], [1,2,3,4,5], [2,3,4,5], [1,3]]

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
	#print(len(P), len(T))
	listOfJays = [] #initialize empty array to hold indices for all itemsets that are the same
	for i in range(len(T)):
		for j in range(i+1, len(T)):
			if(T[i] == T[j]):
				if(compareLists(P[i],P[j])):
					listOfJays.append(j)
	#print(listOfJays)
	#27065, 8048
	#print(P[7880], P[27065], P[8048], P[27066])
	for i in range(len(listOfJays)):
		#del T[listOfJays[i]]
		#del P[listOfJays[i]]
		P[listOfJays[i]] = 0
		T[listOfJays[i]] = 1
		
	#print(P)
	x = len(T)-1
	i = 0
	#print(T)
	'''
	while(i<=x):
		if(P[i] == 0):
			T.pop(i)
			P.pop(i)
			x = x - 1
		if(x < i):
			print("lol")
		i = i + 1
	try:
		P.remove(0)
		T.remove(1)
	except ValueError:
		return
	#list(filter((0).__ne__, P))
	#list(filter(lambda a: a != 0, P))
	'''
	newP = []
	newT = []
	for i in range(len(P)):
		if(P[i] != 0):
			newP.append(P[i])
			newT.append(T[i])
	#print(newP)
	#y = int(input("yikes"))
	return newP, newT

						
def getLevels(R,L,k):
	for n in range(1,len(R)-1):
		#print("Current level", n+1)
		for i in range(len(R[n])):
			for j in range(len(R[1])):
				if(checkExists(R[1][j], R[n][i]) == False): # Fix this to work with lists
					#print(L[n][i], "\n", L[1][j])
					'''
					if(n==1):
						print(L[n][i], "\n", L[1][j])
						y = int(input("yolo bb"))
						
					try:
						New = intersection(L[n][i], L[1][j])
					except TypeError: 
						print("level = ", n+1,"\n", L[n], "\n", R[n], "\n", L[n][i], "\n", L[1][j])
						x = int(input("yolo"))
						'''
					New = intersection(L[n][i], L[1][j])
					if(len(New) >=k):
						#print(New, "   ", len(New))
						#print([R[n][i], R[1][j]])
						#y = int(input("yolo"))
						if(n == 1):
							R[n+1].append([R[n][i], R[1][j]])
						else:
							#print(R[n][i]+R[1][j])
							R[n+1].append( R[n][i] + [ R[1][j] ] )
							#y = int(input("yolo"))
						L[n+1].append(New)
		#print(R[n+1], L[n+1])
		R[n+1], L[n+1] = checkDuplicates(R[n+1], L[n+1])		
		#print(R[n+1], L[n+1])
		print("Level ", n+1, "-->  Length = ", len(R[n+1]) )
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
	print(R[1])
	#print(L[1])
	print("\n")
	#print(len(R[1]))
	
	getLevels(R, L, k)
	

def main():
	A = importCSV('groceries.csv')
	#print(len(A))
	
	N = findUniqueItems(A)
	T = createTransactionFrequency(N, A)

	R = [[] for i in range(6)]
	R[0] = N #first element of R holds all the unique items

	L = [[] for i in range(6)]
	L[0] = T #First element of L holds the TID's associated with each unique item
	#if(checkExists(N[0], A[0])):
		#print("yay")
	#print(checkExists(N[45], A[0]))
	#print(T[0])
	printList(R,L,T,35)

main()

