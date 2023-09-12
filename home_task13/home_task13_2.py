def out_function(x):
    def in_function(y):
        return x + y
    return in_function


in_func_1 = out_function(5)
in_func_2 = out_function(7)


result_1 = in_func_1(6)
result_2 = in_func_2(8)

print("Result 1:", result_1)
print("Result 2:", result_2)
