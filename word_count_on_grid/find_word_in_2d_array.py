# RECURSION => BACKTRACKING => WORD SEARCH COUNT

def word_count(array, index):
    rows= len(array)            #total rows in array
    columns= len(array[0])      #Total no. of elements in first row (how many columns)
    
    
    def backtrack(rows, columns, index):
      
      #where the point fail on rows and columns
      
      if rows>len(rows) OR  columns>len(columns):
        
    
    
