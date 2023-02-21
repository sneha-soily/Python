mydic={
    "fast" : "In a quick manner",
    "Harry": "A coder",
    "Marks": [1,2,3,4,5],
    "another_dict":{'harry':'player'},
    1: 1
}
#print all keys='fast', 'Harry', 'Marks', 'another_dict',1
print(list(mydic.keys())) 
print(mydic.keys()) 
#print all values='In a quick manner', 'A coder', [1, 2, 3, 4, 5], {'harry': 'player'}, 1
print(list(mydic.values()))
print(mydic.values()) 
#print all (keys,value) 
print(list(mydic.items())) 
print(mydic.items()) 

#update dictionary
update_dic={
    "Lovish" : "Friend",
    "divya" : "Friend",
    "Harry": "A dancer"
}
mydic.update(update_dic)
print(mydic)

print(mydic.get("Harry"))
print(mydic["Harry"])

print(mydic.get("Harry2")) #using get method then return none bcz harry2 not present in the dic
print(mydic["Harry2"])  #using this method then return error bcz harry2 not present in the dic