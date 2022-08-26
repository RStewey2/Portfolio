from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from queue import PriorityQueue

data = pd.read_csv('C:/Users/rstew/OneDrive/Documents/NZ_Schools.csv')
data.head()
data.isnull().sum()
y = data['Perf_Category']

X = data.drop(['Perf_Category','Territorial_Authority','Graduating_Students'], axis = 1)
X2 = X
print(f'X : {X.shape}')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=101)
print(f'X_train : {X_train.shape}')
print(f'y_train : {y_train.shape}')
print(f'X_test : {X_test.shape}')
print(f'y_test : {y_test.shape}')
rf_Model = RandomForestClassifier()
rf_Model.fit(X_train, y_train)
print(rf_Model.predict(X_test))
print(rf_Model.predict_proba(X_test))
print("Original Data Frequency Table")
Freq = data.Perf_Category.value_counts("Perf_Category")
print(Freq)
data["Whole_Dollar_Teach_Per_Student"].value_counts("Whole_Dollar_Teach_Per_Student")
cross = pd.crosstab(index=data["Perf_Category"], columns=data["Whole_Dollar_Teach_Per_Student"])
print(cross/cross.sum())
data["Whole_Dollar_NonTeach_Per_Student"].value_counts("Whole_Dollar_NonTeach_Per_Student")
cross = pd.crosstab(index=data["Perf_Category"], columns=data["Whole_Dollar_NonTeach_Per_Student"])
print(cross/cross.sum())
data["Whole_Dollar_Total_Per_Student"].value_counts("Whole_Dollar_Total_Per_Student")
cross = pd.crosstab(index=data["Perf_Category"], columns=data["Whole_Dollar_Total_Per_Student"])
print(cross/cross.sum())



print("The below will predict a Performance Category based on school input: ")
funding = float(input("Enter the total funding in thousands of NZD:"))
t_salaries = float(input("Enter the total funding for teachers salaries in thousands of NZD:"))
student = float(input("Enter the total number of students:"))
t_fund_perc = t_salaries/funding
t_fund_per_pupil = t_salaries/student
WD_t_fund_per_pupil = int(t_fund_per_pupil)
tot_per_stud = funding/student
WD_tot_per_stud = int(tot_per_stud)
Non_teach_per_stud = (funding-t_salaries)/student
WD_non_teach_per_stud = int(Non_teach_per_stud)
data_exp = [[funding, t_salaries, student, t_fund_perc, t_fund_per_pupil, WD_t_fund_per_pupil, WD_tot_per_stud, WD_non_teach_per_stud, tot_per_stud, Non_teach_per_stud]]
df = pd.DataFrame(data_exp, columns = ['Funding', 'Teacher_Salaries','Students','Teacher_Funding_Percent','Teach_Funds_PerPupil','Whole_Dollar_Teach_Per_Student','Whole_Dollar_Total_Per_Student','Whole_Dollar_NonTeach_Per_Student','Total_Funds_PerPupil','NonTeach_Funds_PerPupil'])
print("This proposed school is expected to fall into the category of: ")
print(rf_Model.predict(df))

X_filt=data[(data['Perf_Category']=='Underperforming') & (data['NonTeach_Funds_PerPupil']< 3.5)]

Under_list=X_filt.values



v = len(X_filt.index)+2
graph = [[] for i in range(v)]


def best_first_search(source, target, n):
    visited = [False] * n
    # visited = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print("The school district with the "+str(c)+ " thousand NZD cost should be the primary concern")


# Function for adding edges to graph


def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

target = len(X_filt.index)+1
for x in range(len(X_filt.index)):
    difficulty = (3.5-Under_list[x][10])*Under_list[x][3]
    print(str(difficulty)+" : "+str(x))

    addedge(x,target,int(difficulty))

source = 0
best_first_search(source, target, v)