names=['sujan', 'aalok', 'kabir', 'hemant']
print(names[0] + " how is it going keta")
print(names[1] + " k vairachha sathi OC tira")
print(names[2] + "OHo sathi call navako panni tannai vayo tw")
print(names[-1] + "Khana kasto thiyo hemant pandey")
names[0]='righam'
print(names)
names.append('dipesh')

print(names)

names.insert(0, 'denish')
print(names)
del names[0]
print(names)
popped_element = names.pop()
print (popped_element)


print(names.pop(0) + " is the son of the principal of our school") 
print(names)
print(names.pop(1) + "is my best friend after coming to uS")
