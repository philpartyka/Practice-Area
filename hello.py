string= "Slicing strings is easy!"

print(string[1:-10:2])
print(string[:-1])

string = ['This', 'a', 'list']
string1 = 'yup'
#print(string + string1)
#Above will print an error because you can't add a str with a list
string.pop(1)
print(string)

tuple3 = ("one", "two", "three")
name, number, type = tuple3
print(tuple3[2])

print(list(range(1,8,2)))
#prints odd numbers

target = ['apple','orange','ananas','banana','pear']
sample = ['apple','pear','pineapple','blue']

def transform(target, sample):
    sub = sample.copy()
    for i in sub:
        if i not in target:
            sample.remove(i)
    
    for n,x in enumerate(target):
        if x not in sub:
            sample.insert(n,x)

    return sample

print(transform(target, sample))

def trans(target, sample):
    sample = target.copy()
    return sample

print(trans(target, sample))


dict = {"key1":1, "key2":(2,3)}
print(dict['key2'][0])
print(dict.keys())
print(dict.items())


car = "Lamborghini"

print(car[3:-5])

book = """The Project Gutenberg eBook of The Eagle's eye, by William J. Flynn

This eBook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this eBook or online at
www.gutenberg.org. If you are not located in the United States, you
will have to check the laws of the country where you are located before
using this eBook."""

punctuations = ['!','(',')','-','[',']','{','}',';',':',"'",'"',"\\",",","<",">",'.','/','?','@','#','$','%','^','&','*','_','~']

'''
for word in book.split():
    for char in word:
        if char not in punctuations:
            newword += char
    print(newword)
'''

#punctuations = ['!','(',')','-','[',']','{','}',';',':',"'",'"',"\\",",","<",">",'.','/','?','@','#','$','%','^','&','*','_','~']
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

word_count = {} 
    
for word in book.split():
    #new_word = "".join([char for char in word if char not in punctuations]).lower()
    #Above line is a list comprehension of below for loop
        
    char_list = []
    for char in word:
         if char not in punctuations:
            char_list.append(char)
            new_word = "".join(char_list).lower()
    
    if new_word.isalpha():
        if new_word not in uninteresting_words:
            word_count[new_word] = word_count.get(new_word, 0) + 1


n = 7
fb_list = [0,1]
# for i in range(2,n):
#     fb_list.append(fb_list[i-2]+fb_list[i-1])
[fb_list.append(fb_list[i-2]+fb_list[i-1]) for i in range(2,n)]
#fb_list.extend([fb_list[i-2]+fb_list[i-1] for i in range(2,n)])
print(fb_list)   
#print(new_list) 

print(1.2-1.0)