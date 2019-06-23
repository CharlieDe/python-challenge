import os
import csv

csvpath=os.path.join('Poll.csv')
Results = 'results.txt'
outpath = os.path.join('Results')
cands = []
numV = 0
voteC = []


with open (csvpath, newline="") as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
  
    next(csvread,None)
      
    for row in csvread:        
   
        numV = numV +1
        candidate = row[2]  
          
        if candidate in cands:
            candidate_index = cands.index(candidate)
            voteC[candidate_index] = voteC[candidate_index] + 1
             
        else:
            cands.append(candidate)
            voteC.append(1)

    percentage = []
    masV = voteC[0]
    mc = 0
    
    for count in range(len(cands)):
        voteP = voteC[count]/numV*100
        percentage.append(voteP)
        if voteC[count] > masV:
            masV = voteC[count]
            print(masV)
            mc = count
    winner = cands[mc]
   
    percentage = [round(i,2) for i in percentage]
    

    print("Election Results")
    print("-------------------------------------------")
    print(f"Total Votes: {numV}")
    print("-------------------------------------------")
    for count in range(len(cands)):
        print(f"{cands[count]}: {percentage[count]}% ({voteC[count]})")
    print("-------------------------------------------")
    print(f"Winner: {winner}")
    print("-------------------------------------------")
    
with open(outpath, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("---")
    txt_file.write(f"Total Votes: {numV}")
    txt_file.write("---")
    txt_file.write(f"{cands[count]}: {percentage[count]}% ({voteC[count]})")
    txt_file.write("---")
    txt_file.write(f"Winner: {winner}")
    txt_file.write("---")