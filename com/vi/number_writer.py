# coding:UTF-8
import json

numbers = [1,3,5,7,9,11,13]

filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)
