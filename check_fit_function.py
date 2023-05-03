
def check_fit(row_index, column_index, len_word, size_board, used_indices):
  directions = []
  print('horizontal right ',  not any([(row_index, i)  in used_indices for i in range (column_index, column_index + len_word)]))
  print('horizontal left', not any([(i, column_index)  in used_indices for i in range (row_index, row_index-len_word)]))
  print('vertical up', not any([(i, column_index)  in used_indices for i in range (row_index, row_index-len_word)]))
  print('vertical down', not any([(i, column_index)  in used_indices for i in (row_index, row_index+(len_word))]))
  print('diagonal t to b',not any([(row_index+i, column_index-i)  in used_indices for i in (0, len_word)]))
  print('diagonal b to t', not any([(row_index-i, column_index+i)  in used_indices for i in (0, len_word)]))

  if len_word <= (column_index+1) and not any([(row_index, i)  in used_indices for i in range (column_index, column_index-(len_word))]):
      directions.append('horizontal left')
  
  if column_index + (len_word-1) <= (size_board-column_index) and not any([(row_index, i)  in used_indices for i in range (column_index, column_index + len_word)]):
    directions.append( 'horizontal right')


  if len_word-1 <= row_index and not any([(i, column_index)  in used_indices for i in range (row_index, row_index-len_word)]):
     directions.append('vertical up')
   
  if row_index + (len_word) <= (size_board-row_index) and not any([(i, column_index)  in used_indices for i in (row_index, row_index+(len_word))]):
      directions.append('vertical down')
     
  if  column_index + (len_word-1) <= (size_board-column_index) and len_word-1 <= row_index and not any([(row_index-i, column_index+i)  in used_indices for i in (0, len_word)]):
     directions.append('diagonal bottom to top')

  if row_index + (len_word-1) <= (size_board-row_index) and len_word <= (column_index+1) and not any([(row_index+i, column_index-i)  in used_indices for i in (0, len_word)]):
    directions.append('diagonal top to bottom')
  

  return directions
  print(directions)
