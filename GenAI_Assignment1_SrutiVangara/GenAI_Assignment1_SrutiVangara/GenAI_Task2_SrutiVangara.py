from GenAI_Task1_SrutiVangara import sample_product
categories = [sample_product[2],"Electronics","Cosmetics","Stationary",]
# Convert list to set
categories_set = set(categories)

print("Unique Categories:")
print(categories_set)

# Demonstrate duplicate handling
categories_set.add("Electronics")

print("\nAfter adding duplicate 'Electronics':")
print(categories_set)

# Total unique categories
print("\nTotal Unique Categories:", len(categories_set))