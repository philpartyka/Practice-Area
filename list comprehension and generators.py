#buzz = ["FizzBuzz" if x%15==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else x for x in range(1,101)]

#print(buzz)



def even_n(max_n):
    n = 1
    while n <= max_n: 
        yield n * 2 
        n += 1

i = even_n(3) 
print(next(i))
print(next(i)) 
print(next(i))

print("---")




def prime_gen():
    n = 2
    while True:
        if all(n%p!=0 for p in range(2,n)):
            yield n
        n += 1

gen = prime_gen()
for _ in range(10): 
    print(next(gen), end=' ')

print("---")

def primes_gen():
    n = 2
    while True:
        flag = 0
        i = 2
        while i <= (n/2):
            if (n%i) == 0:
                flag = 1
                break
            i += 1
        if flag == 0:
            yield n
        n += 1

gen = primes_gen()
for _ in range(10): 
    print(next(gen), end=' ')   





# def primes_gens(x=2):
#     #x = 2
#     i = 1
#     while i <= x:
#         if x % i != 0:
#             i += 1
#             continue
#         if x % i == 0 and i < x:
#             x += 1
#             i = 1
#         else:
#             yield x
#             x += 1
#             i = 1

# gen = primes_gens()
# for _ in range(10): 
#     print(next(gen), end=' ')

prog_l = [('Python', 3.10),('Java',13),('JavaScript',2019),('Scala',2.13)]

print(sorted(prog_l, key=lambda x:x[1]))

#below is same as above. lambda allows you to not use an explicit version
def get_version(input_tuple):
    return (input_tuple[1])
print(sorted(prog_l, key=get_version))


print(sorted(prog_l, key=lambda x:len(x[0]), reverse=True))



prog_l = [('c++', 3.10),('Java',13),('JavaScript',2019),('Scala',2.13),('Python',3.10)]
print(sorted(prog_l, key=lambda x:x[1]))
print(sorted(prog_l, key=lambda x:(x[1],x[0])))
#above sorts by the first value(x[1]) and then sorts by the second (x[0])