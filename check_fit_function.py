def check_fit(row_index, column_index, len_word, size_board):
  directions = []
  if len_word <= (column_index):
      directions.append('horizontal left')
  
  if column_index + len_word <= (size_board-column_index):
    directions.append( 'horizontal right')
    
  if len_word <= (row_index):
     directions.append('vertical up')
   
  if row_index + len_word <= (size_board-row_index):
      directions.append('vertical down')
     
  if len_word<= column_index and len_word<= row_index:
     directions.append('diagonal bottom to top')

  if column_index + len_word <= (size_board-column_index) and row_index + len_word <= (size_board-row_index):
    directions.append('diagonal top to bottom')

  print(directions)
