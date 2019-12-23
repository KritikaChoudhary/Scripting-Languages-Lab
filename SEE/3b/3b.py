'''
3b. Python File Handling & List Comprehension: Write a python program to read contents of a file (filename as argument) and store number of occurrences of each word in a dictionary. Display the top 10 words with most number of occurrences in descending order. Store the length of each of these words in a list and display the list. Write a one-line reduce function to get the average length and one-line list comprehension to display squares of all odd numbers and display both.
[] in list comprehension very very important
'''
from functools import reduce
from collections import Counter
def word_count(file):
    with open(file) as f:
        return Counter(f.read().split())

cnt=word_count("sample.txt")
print("Word count:",cnt)
cnt=cnt.most_common()
li=[]
print("Top 10:")
for i in range (10):
    print(cnt[i][0])
    li.append(len(cnt[i][0]))
print(li)

print("Average of the lengths:",reduce(lambda x,y:x+y,li)/len(li))

print([x for x in li if x%2==0])



