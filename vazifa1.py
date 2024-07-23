import os

current_dir = 'C:/Users/YourUsername/Documents/'  
old_file = 'product.xlsx'
new_file = 'my_products.xlsx'

os.rename(os.path.join(current_dir, old_file), os.path.join(current_dir, new_file))