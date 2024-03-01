def enum(**enums):
	return type('Enum' , () ,enums)
	
Num = enum(one = 1 , two = 2 , three ='three')

print(Num.one)
