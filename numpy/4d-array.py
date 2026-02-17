# It's time to more solidfy creating an array concepts in numpy
''' 
🔹 4d Array ✔️
'''

'''  4d Array shape must be (3,2,4,2)
where 3 = second layer/depth
2= first layer after rows and columns
4 is rows and 2 is columns
''' 
import numpy as sam
fourd_array=sam.array([
    [
        [[1,2],
         [4,5],
         [3,4],
         [5,6]],

        [[5,5],
         [4,4],
         [3,3],
         [2,2]]
    ],
    
    [
        [[2,1],
         [3,1],
         [4,1],
         [5,1]],
         
         [[2,5],
          [1,5],
          [3,5],
          [4,5]]
    ],
    [
        [[1,4],
         [2,4],
         [3,4],
         [5,4]], 
         
         [[1,0],
          [2,0],
          [3,0],
          [4,0]]
    ]
])

print(fourd_array.shape)