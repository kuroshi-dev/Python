arr = [1, 2, 3, 4, 5] # basic list, why not?

print("Task 3: List Operations")
print("List:", arr)

min_element = min(arr)
print(f"Minimum element: {min_element}")

sum_arr_positive = sum(i for i in arr if i > 0 and i % 2 != 0) # init var, then get sume for each if var / 0 not 0
print(f"Sum of positive odd elements: {sum_arr_positive}") # i find a way for compact code :D but it less readable

positive_elements = [i for i in arr if i > 0] 
print(f"Positive elements: {positive_elements}")
