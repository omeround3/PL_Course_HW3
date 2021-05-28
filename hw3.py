import random

list_of_types = [['a','b',3],[4,5]]
list_of_numbers = [1,5,6,7,2]

#q1
def list_of_types_checker(list_of_types):
    return sum(map(lambda x: all(isinstance(i, type(x[0])) for i in x[1:]),list_of_types))

#q2
vlst = ['x'+str(num) for num in range(10)]
lamdic = {}
for i,l in enumerate(vlst):
 lamdic[l] = lambda num: (int(v.replace('x', '')) + 1) * num
for v in vlst:
    for i in range(1,len(vlst)+1):
        print(lamdic[v](i),end=' ')
    print()

#q3

class a():
    z=0
    def __init__(self, y):
        self.y = y
    def __call__(self, z):
        if z > self.y:
            return z-self.y
        else:
            return self.y-z
class b(a):
    def __call__(self, z=4):
        if z > self.y:
            return z-self.y
        else:
            return self.y-z
        
print(a(5)(b(6)()))
print(a(6)(b(5)(6)))


#q4
def sort_list_with_lambda(list_of_numbers):
    return sorted(list_of_numbers)

#q5-a-b
def call_counter(func):
    def helper(*args , **kargs):
        call_counter.total_count += 1
        helper.calls += 1
        helper.params += (len(args)+len(kargs))
        print(f"calls for current:{helper.calls}")
        print(f"params for current:{helper.params}")
        print(f"total invokes: {call_counter.total_count}")
        func_type  = type(func(*args,**kargs)).__name__
        call_counter.types[func_type] = call_counter.types.get(func_type , 0) + 1
        print(call_counter.types)
        return func(*args, **kargs)
    helper.calls = 0
    helper.params = 0
    call_counter.total_count = 0
    call_counter.types = {}
    return helper

@call_counter
def succ(x):
    return x+1

@call_counter
def fail(x):
    return str(x+1)


#q7
def a():
    rand_number = random.randint(1, 5)
    c_function = c()
    b2_function = b2()
    b3_function = b3()
    c_function.__next__()
    b2_function.__next__()
    b3_function.__next__()
    b2_function.send(c_function)
    b3_function.send(c_function)
    c_function.send(rand_number)
    b2_function.send(rand_number)
    b3_function.send(rand_number)

def b2():
    function_c = yield
    while True:
        a_number = yield
        powed_number = pow(a_number, 2)
        function_c.send(powed_number)

def b3():
    function_c = yield
    while True:
        a_number = yield
        powed_number = pow(a_number, 3)
        function_c.send(powed_number)

def c():
    while True:
        a_number = yield
        b2_number = yield
        b3_number = yield
        sum_b2_b3 = b2_number+ b3_number
        function_c.send(powed_number)
        print(f"A number: {a_number} , sum of b2, b3: {sum_b2_b3}")

succ(1)
succ(0)
fail(0)
succ(1)
print(succ.calls)
print(fail.calls)

print(list_of_types_checker(list_of_types))
print(sort_list_with_lambda(list_of_numbers))
