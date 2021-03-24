import csv
from itertools import permutations

def importCSV(file):
	with open(file, 'r') as groceries_obj:
		groceries_csv = csv.reader(groceries_obj)
		list_of_rows = list(groceries_csv)
		return list_of_rows

def checkExists(item, dictionary):
	if(item in dictionary):
		return True
	return False

def findLongest(list):
	max = 0
	for i in range(len(list)):
		if len(list[i]) > max:
			max = len(list[i])
	return max

def createItemset(itemList, k):
	itemsetList = []
	for i in range(k):
		kItemset = []
		for j in range(1, len(itemList)):
			if(len(itemList) >= k):
				tempPermutations = list(permutations(itemList[j], i))
			#print(list(tempPermutations))
				for j_ in range(len(tempPermutations)):
					if(checkExists(tempPermutations[j_], kItemset) == False):
						kItemset.append(tempPermutations[j_])
		print(kItemset)
		itemsetList.append(kItemset)
	return itemsetList


def findUniqueItems(A):
	B = []
	for i in range(len(A)):
		for j in range(len(A[i])):
			if(checkExists(A[i][j], B) == False):
				B.append(A[i][j])

def main():
	A = importCSV('groceries.csv')
	B = findUniqueItems(A)
	maxK = findLongest(A)
	finList = createItemset(A, maxK)
	#print(finList)
	
	

main()