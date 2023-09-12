def number_variables():
    var1 = 5
    var2 = 'word'
    var3 = [10, 20, 25]

    local_variables = locals()
    return local_variables

result = number_variables()
print(len(result))