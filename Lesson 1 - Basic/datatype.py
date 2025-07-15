# Cú pháp lấy data type
x = 10
y = type(x)
print (y)

# Các kiểu dữ liệu
x = "Hello World"	                            #str	
x = 20	                                        #int	
x = 20.5	                                    #float	
x = 1j	                                        #complex	
x = ["apple", "banana", "cherry"]	            #list	
x = ("apple", "banana", "cherry")	            #tuple	
x = range(6)	                                #range	
x = {"name" : "John", "age" : 36}	            #dict	
x = {"apple", "banana", "cherry"}	            #set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                                    #bool	
x = b"Hello"	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview	
x = None	                                    #NoneType	

# Ép kiểu
x = float (20)