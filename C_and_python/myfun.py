import ctypes
NUM = 16
A=5
B=6
fun = ctypes.CDLL("C:\\Users\\HARSH WARDHANA\\Desktop\\C_and_python\\libfun.dll")
fun.myFunction.argtypes = [ctypes.c_int]
returnVale = fun.myFunction(NUM)
print(returnVale)
fun.connect()

#fun.sum.argtypes=[ctypes.c_int,ctypes.c_int]
sum_value=fun.sum(A,B)
print("\nSum of the number given by you is : \t")
print(sum_value)
