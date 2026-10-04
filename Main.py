marks = []
with open("scores.txt") as file:
    scores = file.readlines()
    for score in scores:
        if int(score)>90:
            marks.append(score)

with open("high_scores.txt","w") as file:
    for score in marks:
        file.write(score)
  

        
        
    
    
