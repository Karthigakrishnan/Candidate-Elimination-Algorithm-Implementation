import numpy as np 
import pandas as pd 

# Load dataset
data = pd.read_csv('/content/enjoysport.csv') 

# Extract concepts and target
concepts = np.array(data.iloc[:, :-1]) 
target = np.array(data.iloc[:, -1]) 

def learn(concepts, target): 
    specific_h = concepts[0].copy() 
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))] 
    
    for i, h in enumerate(concepts): 
        if target[i].lower() == "yes":   # positive example
            for x in range(len(specific_h)): 
                if h[x] != specific_h[x]: 
                    specific_h[x] = '?' 
                    general_h[x][x] = '?' 
            print("\nFor Training instance No:{0} the hypothesis is".format(i)) 
            print("Specific Hypothesis: ", specific_h) 
            print("General Hypothesis: ", general_h) 

        elif target[i].lower() == "no":  # negative example
            for x in range(len(specific_h)): 
                if h[x] != specific_h[x]: 
                    general_h[x][x] = specific_h[x] 
                else: 
                    general_h[x][x] = '?' 
            print("\nFor Training instance No:{0} the hypothesis is".format(i)) 
            print("Specific Hypothesis: ", specific_h) 
            print("General Hypothesis: ", general_h) 

    # Remove fully generic hypotheses
    general_h = [g for g in general_h if g != ['?', '?', '?', '?', '?', '?']] 

    return specific_h, general_h 


print("*" * 20, "Candidate Elimination Algorithm", "*" * 20) 
s_final, g_final = learn(concepts, target) 
print("\nFinal Specific hypothesis:", s_final) 
print("Final General hypothesis:", g_final)
