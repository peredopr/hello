scores = []
for i in range(3):
    score = int(input("Score: "))
    scores.append(score)  #append (attach) the value of prompt into the scores list
    #scores += [score]

average = sum(scores) / len(scores)
print(f"Average: {average}")