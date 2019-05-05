# DataStructure
This repo consists datastructure parctises mostly written mostly in python
# Big O notation 
simply means Bigger the size of input, how much it slows down
  a) o(n) -> Linear Time
     def insert_box(boxes):
        for box in boxes:
            print(box) // o(n) n number of operation is done no matter 
  b) o(1) -> Constant time 
     def insert_box(boxes):
        for box in boxes.items:
            print(box[0]) // o(1) always increase one operations no matter 
    
    def insert_box(boxes):
        for box in boxes.items:
            print(box[0]) // o(1)  
            print(box[1]) // o(1) 
            // o(2) always two operations at a time
            