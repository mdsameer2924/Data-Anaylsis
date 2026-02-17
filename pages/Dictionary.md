- ```python
  #duplicated key not support and last value store only
  dict1= {
    'a':4,
    'b':5,
    'c':6,
    'a':7,
    'b':9   
  }
  ```
- ```python
  dic2={"apple":5,"banana":6}
  ##dic2=list(dic2)
  ##for i in dic2:
  ##    dic2=dict(dic2)
  ##    print(f"the fruit is {i} and the quanitity is dic2['apple']")
  ##
  ##for fruit,quantity in dic2.items():
  ##    print("The fruit is",fruit,"and the quantity is",quantity)
      
  ## 2nd method
  for fruit in dic2:
      print("The Fruit is",fruit,"and quantity is", dic2[fruit])
      
  
  ```