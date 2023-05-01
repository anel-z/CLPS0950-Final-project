def check_fit(row_index, column_index, len_word, size_board, used_indices):
  directions = []
  if len_word <= (column_index) and [(row_index, i) not in used_indices for i in range (column_index, column_index-len_word)]:
      directions.append('horizontal left')
  
  if column_index + len_word <= (size_board-column_index) and [(row_index, i) not in used_indices for i in range (column_index, column_index + len_word)]:
    directions.append( 'horizontal right')


  if len_word <= (row_index) and [(i, column_index) not in used_indices for i in range (row_index, row_index-len_word)]:
     directions.append('vertical up')
   
  if row_index + len_word <= (size_board-row_index) and [(i, column_index) not in used_indices for i in (row_index, row_index+len_word)]:
      directions.append('vertical down')
     
  if len_word<= column_index and len_word<= row_index and [(row_index+i, column_index+i) not in used_indices for i in (0, len_word)]:
     directions.append('diagonal bottom to top')

  if column_index + len_word <= (size_board-column_index) and row_index + len_word <= (size_board-row_index) and [(row_index-i, column_index-i) not in used_indices for i in (0, len_word)]:
    directions.append('diagonal top to bottom')
 
  return directions
  print(directions)
