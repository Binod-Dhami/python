#sting.key method
a={'binod' : 'who lives in samll but beautiful named durgauli',
      'school':'rme',
      'marks':[1,13,32,13],
      'anotherdic': {'code with':'harry'
}
}
print(a.keys())
#to identify type 
print(type(a.keys()))
#string.value method
print(a.values())
#.items
print(a.items())#its print all contain of dictionaary
b={     #update the dictionary
    'dibya':"docter to be"
}
a.update(b)
print(a)
#.get
print(a.get('binod'))#return the value

#differnt between .get and []syntax in dictionary
print(a.get('binod2'))#return none as there is no binpd2
print(a['binod2'])#through an error as binod2 is present in a dictionary