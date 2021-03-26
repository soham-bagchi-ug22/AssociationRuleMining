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
			if(checkExists(uniqueItems[i], transactionList[j]) == False):
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
	print(len(P), len(T))
	listOfJays = []
	for i in range(len(T)):
		for j in range(1, len(T)):
			if(T[i] == T[j]):
				if(compareLists(P[i],P[j])):
					listOfJays.append(j)
	#print(listOfJays)
	#27065, 8048
	print(P[7880], P[27065], P[8048], P[27066])
	for i in range(len(listOfJays)):
		#del T[listOfJays[i]]
		#del P[listOfJays[i]]
		T[listOfJays[i]] = 0

	x = len(T)-1
	i = 0
	while(i!=x):
		if(T[i] == 0):
			del T[i], P[i]
			x = x - 1
		if(x < i):
			print("lol")
		i = i + 1

						
def getLevels(R,L,k):
	for n in range(1,len(R)-1):
		for i in range(len(R[n])):
			for j in range(len(R[1])):
				if(R[n][i].find(R[1][j]) == -1): # Fix this to work with lists
					New = intersection(L[n][i], L[1][j])
					#print(New)
					if(len(New) >=k):
						if(n == 1):
							R[n+1].append([R[n][i], R[1][j]])
						else:
							R[n+1].append(R[n][i]+R[1][j])
						L[n+1].append(New)
		checkDuplicates(R[n+1], L[n+1])		
		print("Level ", n+1, "-->  Length = ", len(R[n+1]) )
		print(R[n+1])
		#print(L[n+1])
		print("\n")


def printList(R, L, T, k):
	
	for i in range(len(R[0])):
		if(len(T[i]) >= k):
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
	R[0] = N

	L = [[] for i in range(6)]
	L[0] = T


	printList(R,L,T,7)

main()