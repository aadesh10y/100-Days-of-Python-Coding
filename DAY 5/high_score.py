total_scores = [67,89,98,78,67,56,56,78,99,90,80,85,69,]
# total = sum(total_scores)
# print(total)

sum = 0
for i in total_scores:
    sum += i
    
print(sum)    

# print(max(total_scores))

max = 0
for i in total_scores:
    if i > max:
        max = i
print(max)        