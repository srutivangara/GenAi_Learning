prices = [100,250,400.1200,50,2000,850]
list_grt_500 = list(filter(lambda p:p>500 , prices))
list_lst_500 = list(filter(lambda p:p<=500 , prices))
print("List of prices greater than 500:",list_grt_500)
print("List of prices less than or equal to 500:",list_lst_500)