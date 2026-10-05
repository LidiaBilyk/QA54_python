#filter((func->bool)/condition, iter) == predicate.  Can accept two iters.
numbers = [1,2,3,4,5,6,7,8,9,10]
even_number = filter(lambda x: x%2 == 0, numbers)
print(list(even_number))