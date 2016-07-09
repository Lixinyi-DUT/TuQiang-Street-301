''' 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer. '''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count=dict()
for line in handle:
    if line.startswith('From '):
        temp=line.split()
        count[temp[1]] = count.get(temp[1],0)+1

fre_eamil=None

for email in count:
    if fre_eamil is None or count[email]>count[fre_eamil]:
        fre_eamil=email

print fre_eamil,count[fre_eamil]
