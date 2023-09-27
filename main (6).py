"""
Write a function called linear_search_product that takes the list of produts and a target product
name as input. The function should perform a linear search find the prouct in the list and 
return a list of indices of all occurences of the product if found, or an empty list if the product is 
not found.
"""


def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product  == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sanal", "shoes"]
target = "shoes"
result = linearSearchProduct(products, target)
print(result)



