
def check_fit(row_index, column_index, len_word, size_board, used_indices):
  directions = []
  print('horizontal right ',  [(row_index, i) for i in range (column_index, column_index + len_word)], not any([(row_index, i)  in used_indices for i in range (column_index, column_index + len_word)]))
  print((column_index, column_index + len_word))
  print('horizontal left', [(row_index, i) for i in range (column_index-len_word +1, column_index +1)], not any([(i, column_index)  in used_indices for i in range (row_index, row_index-len_word)]))
  print(column_index-len_word +1, column_index +1)
  print('vertical up', [(i, column_index) for i in range (((row_index+1)-len_word), (row_index+1))]), not any([(i, column_index) in used_indices for i in range (((row_index+1)-len_word), (row_index+1))])
  print(row_index, (row_index-len_word))
  print('vertical down',  [(i, column_index) for i in range (row_index, (row_index+len_word))], not any([(i, column_index)  in used_indices for i in (row_index, row_index+(len_word))]))
  print(row_index, row_index+(len_word))
  print('diagonal t to b', [(row_index+i, column_index-i) for i in range(0, len_word)], not any([(row_index+i, column_index-i)  in used_indices for i in (0, len_word)]))
  print(0, len_word)
  print('diagonal b to t', [(row_index-i, column_index+i) for i in range(0, len_word)] , not any([(row_index-i, column_index+i)  in used_indices for i in (0, len_word)]))
  print(0, len_word)
  if len_word <= (column_index+1) and not any([(row_index, i)  in used_indices for i in range (column_index-len_word +1, column_index +1)]):
      directions.append('horizontal left')
  
  if column_index + (len_word-1) <= (size_board-column_index) and not any([(row_index, i) in used_indices for i in range (column_index, column_index + len_word)]):
    directions.append( 'horizontal right')


  if len_word-1 <= row_index and not any([(i, column_index) in used_indices for i in range (((row_index+1)-len_word), (row_index+1))]):
     directions.append('vertical up')
   
  if row_index + (len_word) <= (size_board-row_index) and not any([(i, column_index) in used_indices for i in range (row_index, (row_index+len_word))]):
      directions.append('vertical down')
     
  if  column_index + (len_word-1) <= (size_board-column_index) and len_word-1 <= row_index and not any([(row_index-i, column_index+i)  in used_indices for i in range (0, len_word)]):
     directions.append('diagonal bottom to top')

  if row_index + (len_word-1) <= (size_board-row_index) and len_word <= (column_index+1) and not any([(row_index+i, column_index-i)  in used_indices for i in range (0, len_word)]):
    directions.append('diagonal top to bottom')
  

  return directions
  print(directions)
