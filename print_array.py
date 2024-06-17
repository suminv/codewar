def print_array(array):
    return ','.join(map(str, array))



print(print_array(["h","o","l","a"]))
print(print_array(["2","4","5","2"]))
print(print_array([[True,False,False]])) #[True,False,False]
print(print_array([2,4,5,2])) # "2,4,5,2"