# Candidate Elimination Algorithm

This project implements the **Candidate Elimination Algorithm** in Python using `numpy` and `pandas`.  
The algorithm learns the **specific** and **general hypotheses** from a given dataset (`enjoysport.csv`) based on positive and negative training examples.

---

## 📂 Files in the Project
- **candidate_elimination.py** → Python script containing the algorithm implementation.  
- **enjoysport.csv** → Example dataset used for training the algorithm.  
- **README.md** → Documentation file (this file).

---

## 📊 Dataset Format (enjoysport.csv)
The dataset should contain attribute values with the final column as the **target** (Yes/No).  

Example:

| Sky   | AirTemp | Humidity | Wind   | Water | Forecast | EnjoySport |
|-------|---------|----------|--------|-------|----------|------------|
| Sunny | Warm    | Normal   | Strong | Warm  | Same     | Yes        |
| Sunny | Warm    | High     | Strong | Warm  | Same     | Yes        |
| Rainy | Cold    | High     | Strong | Warm  | Change   | No         |
| Sunny | Warm    | High     | Strong | Cool  | Change   | Yes        |

---

## ⚙️ How It Works
1. Load the dataset using `pandas`.
2. Extract:
   - **Concepts** → All attributes except the target column.  
   - **Target** → The last column (Yes/No).
3. Initialize:
   - **Specific Hypothesis (S)** → First positive training example.  
   - **General Hypothesis (G)** → Most general hypothesis (all `?`).
4. For each training instance:
   - If **positive (Yes)** → Generalize the specific hypothesis.  
   - If **negative (No)** → Specialize the general hypothesis.  
5. At the end, output the final **Specific (S)** and **General (G)** hypotheses.

---
******************** Candidate Elimination Algorithm ********************

For Training instance No:0 the hypothesis is
Specific Hypothesis:  ['Sunny' 'Warm' 'Normal' 'Strong' 'Warm' 'Same']
General Hypothesis:  [['?', '?', '?', '?', '?', '?'],
                     ['?', '?', '?', '?', '?', '?'],
                     ['?', '?', '?', '?', '?', '?'],
                     ['?', '?', '?', '?', '?', '?'],
                     ['?', '?', '?', '?', '?', '?'],
                     ['?', '?', '?', '?', '?', '?']]

...

Final Specific hypothesis: ['Sunny' 'Warm' '?' 'Strong' '?' '?']
Final General hypothesis: [['Sunny', '?', '?', '?', '?', '?']]
