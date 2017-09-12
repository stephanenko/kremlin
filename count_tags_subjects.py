'''
We count the frequency of mentioned in articles subjects.
What are the most popular?
'''

from collections import Counter
with open('subjectsTAG.txt', 'r') as f:
    out = ''
    p = f.read() # p contains contents of entire file
    p = p.strip()
    p = p.replace("  ", "")
    p = p.replace("«", "")
    p = p.replace("»", "")
    p = p.replace(", ",',')

    words = p.replace('\n', ',').split(',')
    print(words)
    wordCount = len(words)
    print ("The total word count is:", wordCount)
    N = int(input("How many words do you want?"))

    c = Counter(words)
    for w, count in c.most_common(N):
        if len(w) > 2:
            out = str(w) + ',' + str(count)
            print (out)