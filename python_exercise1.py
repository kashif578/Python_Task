# -*- coding: utf-8 -*-
"""python exercise1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ok7SSCh5Zj98WT56kSAEgdKR8Au0iU_0

1. convert string into list of list with first line as first element in all sublist, sublist len is 3
	ex:    input:        in string
				first line 
				second line 
				third line
				fourth line
				fifth line
				
			output:
			    [["first line", "second line", "third line"], ["first line", "fourth line", "fifth line"]]
"""

input_string='''first line 
second line 
third line
fourth line
fifth line'''         
newlist = input_string.split('\n')
list_1=[newlist[0],newlist[1],newlist[2]]
list_2=[newlist[0],newlist[3],newlist[4]]
list_of_list=[list_1,list_2]
print(list_of_list)

"""2. Parse below output to form dictionary where output should be like {key: []}
    ex:     input:       in string
	            device1   vlan1
				device2   vlan2
				device3   vlan1
				device2   vlan3
				device1   vlan4
				device2   vlan1
				device3   vlan6
			
			output: 
			    {"device1": ["vlan1", "vlan4"], "device2": ["vlan2", "vlan1", "vlan3"], "device3": ["vlan1", "vlan6"]}
"""

input_string ="""device1   vlan1
		device2   vlan2
		device3   vlan1
		device2   vlan3
		device1   vlan4
		device2   vlan1
		device3   vlan6 """
dictonary={}
for subString in input_string.split("\n\t\t"):
    
    l = list(subString.split("   "))
    if l[0] in dictonary:
        dictonary[l[0]].append(l[1])
    else:
        dictonary[l[0]] = list(l[1].split(" "))

print(dictonary)

my_dic={'stream_group01': {'stream_group01-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '219874', 'Rx Frames': '1978866', 'Loss %': '', 'Frames Delta': '1758992', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '9000.000'}}, 'stream_group02': {'stream_group02-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '209257', 'Rx Frames': '1255542', 'Loss %': '', 'Frames Delta': '1046285', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '6000.000'}}}
print('Transmitted rate is',my_dic['stream_group01']['stream_group01-EndpointSet-1 - Flow Group 0001']['Tx Frame Rate'],'and Received rate is',my_dic['stream_group01']['stream_group01-EndpointSet-1 - Flow Group 0001']['Rx Frame Rate'],'on stream_group01-EndpointSet-1 - Flow Group 0001 of stream_group01')
print('Transmitted rate is',my_dic['stream_group01']['stream_group01-EndpointSet-1 - Flow Group 0001']['Tx Frame Rate'],'and Received rate is',my_dic['stream_group01']['stream_group01-EndpointSet-1 - Flow Group 0001']['Rx Frame Rate'],'on stream_group01-EndpointSet-1 - Flow Group 0001 of stream_group02')



string='''device1   vlan1
device2   vlan2
device3   vlan1
device2   vlan3
device1   vlan4
device2   vlan1
device3   vlan6'''

"""write a class with method to take 2 possitional arguments, 2 key word arguments with one having default value of 0, args, and kwargs and print the arguments and keyword arguments passed on different conditions

    ex:
    Considering as object created with the classwritten
    obj = <class>
    obj.print_func(1,2,a=4,b=5,"a", "c", 45, m="d", l=5)
    output = parameters received are 1, 2
    positional args are 4, 5
    args are ["a", "c" 45]
    kwargs are {m: "d", l=5}
    obj.print_func(1,2,a=4,b=5,"a", "c", 45, m="d", l=5)
    obj.print_func(1,2,a=4,"a", 45, m="d", l=5)
"""