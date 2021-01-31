
import numpy as np
import pandas as pd
import  matplotlib.pyplot  as  plt
import  contextlib import  inflect import  sqlalchemy
engine  =  sqlalchemy.create_engine('mysql+pymysql://root:root@localhost/student')

while  True:
print("  ----------WELCOME  TO  STUDENT  RESULT  MANAGEMENT  ANALYSIS-----------")
print("OPERATIONS:-")
print("1.Show  All  Students  Name  and  Roll  Number  List  of  Class  A  and  Class  B") print("2.Show  All  Students  Marks  List  of  Class  A  and  Class  B")
print("3.Show  Average  Marks  Of  Students  In  Each  Subject") print("4.Show  Highest  Scores  In  Each  Subject") print("5.Show  Lowest  Scores  In  Each  Subject") print("6.Show  Subject  Wise  Pass  Percentage")
print("7.Highest  and  Lowest  Scorer  From  Class  A  and  Class  B") print("8.Show  result  of  particular  student")
print("9.Exit")
print('\n')
choice  =  input("Enter  choice  of  operation  want  to  perform:  ") print('\n')

data  =  pd.read_sql_table('tea',  engine) data1  =  pd.read_sql_table('teb',  engine)

data2  =  data.dropna() data3  =  data1.dropna()

if  (choice  ==  '1'):
print("	Divison  A
")
print(data[["Roll_No","Name"]]) print('\n')
print("Total  Number  of  Students  from  Class  A  :  ",  data.Name.count())

print('\n')
print("	Divison  B
")
print(data1[["Roll_No",  "Name"]]) print('\n')
print("Total  Number  of  Students  from  Class  B  :  ",  data1.Name.count())

if  (choice  ==  '2'):
print("	Divison  A
")
print(data2) print('\n')
print("Total  Number  of  Present  Students  for  Exam  from  Class  A  :  ",
data2.Name.count())
print('\n')
print("	Divison  B
")
print(data3) print('\n')
print("Total  Number  of  Present  Students  For  exam  from  Class  B  :  ",
data3.Name.count())
 
if  (choice  ==  '3'):
print("\n*****Average  Marks  Class  A*****") avga1  =  data2.TOC.mean()
print("\nAverage  Marks  in  TOC  Subject:  ",  avga1)

avga2  =  data2.DBMS.mean()
print("\nAverage  Marks  in  DBMS  Subject:  ",  avga2)

avga3  =  data2.SEPM.mean()
print("\nAverage  Marks  in  SEPM  Subject:  ",  avga3)

avga4  =  data2.ISEE.mean()
print("\nAverage  Marks  in  ISEE  Subject:  ",  avga4)

avga5  =  data2.CN.mean()
print("\nAverage  Marks  in  CN  Subject:  ",  avga5)

#  Average  Marks  Class  B print("\n\n\n*****Average  Marks  Class  B*****") avgb1  =  data3.TOC.mean()
print("\nAverage  Marks  in  TOC  Subject:  ",  avgb1)

avgb2  =  data3.DBMS.mean()
print("\nAverage  Marks  in  DBMS  Subject:  ",  avgb2)

avgb3  =  data3.SEPM.mean()
print("\nAverage  Marks  in  SEPM  Subject:  ",  avgb3)

avgb4  =  data3.ISEE.mean()
print("\nAverage  Marks  in  ISEE  Subject:  ",  avgb4)

avgb5  =  data3.CN.mean()
print("\nAverage  Marks  in  CN  Subject:  ",  avgb5,"\n")


x  =  ['TOC',  'DBMS',  'SEPM',  'ISEE',  'CN']
y  =  [avga1,  avga2,  avga3,  avga4,  avga5]

plt.plot(x,  y,  color='orange',  label="Class  A",  marker='*') y1  =  [avgb1,  avgb2,  avgb3,  avgb4,  avgb5]
plt.plot(x,  y1,  label="Class  B",  marker='o')

plt.legend()
#  naming  the  x  axis plt.xlabel('Subjects') #  naming  the  y  axis plt.ylabel('Marks')
#  giving  a  title  to  my  graph plt.title('Average  Marks  of  Class  A  and  B') plt.show()

if(choice  ==  '4'):
print("\nHighest  Marks  Per  Subject") h1=input(str("Enter  Division  :  "))

if  (h1=='a'  or  h1=='A'):
print("	TOC  ")
 
a  =  data2.TOC.max()
print("Highest  score  in  TOC  subject  From  class  A:\n") d1  =  data2[data2.TOC  ==  a]
print(d1[['Name',  'TOC']].reset_index(drop=True))

plt.title("TOC  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") d1['TOC'].plot.bar()
plt.show()

print('\n')
print("	DBMS  ")
a1  =  data2.DBMS.max()
print("Highest  score  in  DBMS  subject  From  class  A:\n") d2  =  data2[data2.DBMS  ==  a1]
print(d2[['Name',  'DBMS']].reset_index(drop=True))

plt.title("DBMS  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") d2['DBMS'].plot.bar()
plt.show()

print('\n')
print("	SEPM  ")
a3  =  data2.SEPM.max()
print("Highest  score  in  SEPM  subject  From  class  A:\n") d3  =  data2[data2.SEPM  ==  a3]
print(d3[['Name',  'SEPM']].reset_index(drop=True))

plt.title("SEPM  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") d3['SEPM'].plot.bar()
plt.show()

print('\n')
print("	ISEE")
a4  =  data2.ISEE.max()
print("Highest  score  in  ISEE  subject  From  class  A:\n") d4  =  data2[data2.ISEE  ==  a4]
print(d4[['Name',  'ISEE']].reset_index(drop=True))

plt.title("ISEE  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") d4['ISEE'].plot.bar()
plt.show()

print('\n')
print("	CN")

a5  =  data2.CN.max()
print("Highest  score  in  CN  subject  From  class  A:\n") d5  =  data2[data2.CN  ==  a5]
print(d5[['Name',  'CN']].reset_index(drop=True)) plt.title("CN  Subject(Class  A)")
 
plt.xlabel("Roll_No") plt.ylabel("Marks") d5['CN'].plot.bar() plt.show()

elif  (h1=='b'  or  h1=='B'): print('\n')
print("	TOC  ")
b  =  data3.TOC.max()
print("\nHighest  score  in  TOC  subject  From  class  B:\n  ") d6  =  data3[data3.TOC  ==  b]
print(d6[['Name',  'TOC']].reset_index(drop=True))

plt.title("TOC  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") d6['TOC'].plot.bar()
plt.show()

print('\n')
print("	DBMS  ")
b1  =  data3.DBMS.max()
print("\nHighest  score  in  DBMS  subject  From  class  B:\n") d7  =  data3[data3.DBMS  ==  b1]
print(d7[['Name',  'DBMS']].reset_index(drop=True))

plt.title("DBMS  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") d7['DBMS'].plot.bar()
plt.show()

print('\n')
print("	SEPM  ")
b3  =  data3.SEPM.max()
print("\nHighest  score  in  SEPM  subject  From  class  B:\n") d8  =  data3[data3.SEPM  ==  b3]
print(d8[['Name',  'SEPM']].reset_index(drop=True))

plt.title("SEPM  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") d8['SEPM'].plot.bar()
plt.show()

print('\n')
print("	ISEE")
b4  =  data3.ISEE.max()
print("\nHighest  score  in  ISEE  subject  From  class  B:\n") d9  =  data3[data3.ISEE  ==  b4]
print(d9[['Name',  'ISEE']].reset_index(drop=True))

plt.title("ISEE  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") d9['ISEE'].plot.bar()
plt.show() print('\n')
 
print("	CN")
b5  =  data3.CN.max()
print("\nHighest  score  in  CN  subject  From  class  B:\n") d10  =  data3[data3.CN  ==  b5]
print(d10[['Name',  'CN']].reset_index(drop=True))

plt.title("CN  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") d10['CN'].plot.bar()
plt.show()
else:
print("\nInvalid  Choice  !!!  Please  Enter  Class  'A'  or  'B'\n")

if  (choice  ==  '5'):
print("\nLowest  Marks  Per  Subject") l1  =  input(str("Enter  Division  :  "))

if  (l1  ==  'a'  or  l1  ==  'A'): print('\n')
print("	TOC")
A  =  data2.TOC.min()
print("Lowest  score  in  TOC  subject  From  class  A:\n") p1  =  data2[data2.TOC  ==  A]
print(p1[['Name',  'TOC']].reset_index(drop=True))

plt.title("TOC  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") p1['TOC'].plot.bar()
plt.show()

print('\n')
print("	DBMS")
A1  =  data2.DBMS.min()
print("Lowesr  score  in  DBMS  subject  From  class  A:\n") p2  =  data2[data2.DBMS  ==  A1]
print(p2[['Name',  'DBMS']].reset_index(drop=True))

plt.title("DBMS  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") p2['DBMS'].plot.bar()
plt.show()

print('\n')
print("	SEPM")
A3  =  data2.SEPM.min()
print("Lowest  score  in  SEPM  subject  From  class  A:\n") p3  =  data2[data2.SEPM  ==  A3]
print(p3[['Name',  'SEPM']].reset_index(drop=True))

plt.title("SEPM  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") p3['SEPM'].plot.bar()
plt.show() print('\n')
 
print("	ISEE")
A4  =  data2.ISEE.min()
print("Lowest  score  in  ISEE  subject  From  class  A:\n") p4  =  data2[data2.ISEE  ==  A4]
print(p4[['Name',  'ISEE']].reset_index(drop=True))

plt.title("ISEE  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") p4['ISEE'].plot.bar()
plt.show()

print('\n')
print("	CN")
A5  =  data2.CN.min()
print("Lowest  score  in  CN  subject  From  class  A:\n") p5  =  data2[data2.CN  ==  A5]
print(p5[['Name',  'CN']].reset_index(drop=True))

plt.title("CN  Subject(Class  A)") plt.xlabel("Roll_No") plt.ylabel("Marks") p5['CN'].plot.bar()
plt.show()

elif(l1=='b'  or  l1=='B'): print('\n')
print("	TOC")
B  =  data3.TOC.min()
print("\nLowest  score  in  TOC  subject  From  class  B:\n  ") p6  =  data3[data3.TOC  ==  B]
print(p6[['Name',  'TOC']].reset_index(drop=True))

plt.title("TOC  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") p6['TOC'].plot.bar()
plt.show()

print('\n')
print("	DBMS")
B1  =  data3.DBMS.min()
print("\nLowest  score  in  DBMS  subject  From  class  B:\n") p7  =  data3[data3.DBMS  ==  B1]
print(p7[['Name',  'DBMS']].reset_index(drop=True))

plt.title("DBMS  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") p7['DBMS'].plot.bar()
plt.show()

print('\n')
print("	SEPM")
B3  =  data3.SEPM.min()
print("\nLowest  score  in  SEPM  subject  From  class  B:\n") p8  =  data3[data3.SEPM  ==  B3]
print(p8[['Name',  'SEPM']].reset_index(drop=True))
 
plt.title("SEPM  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") p8['SEPM'].plot.bar()
plt.show()

print('\n')
print("	ISEE")
B4  =  data3.ISEE.min()
print("\nLowest  score  in  ISEE  subject  From  class  B:\n") p9  =  data3[data3.ISEE  ==  B4]
print(p9[['Name',  'ISEE']].reset_index(drop=True))

plt.title("ISEE  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") p9['ISEE'].plot.bar()
plt.show()

print('\n')
print("	CN")
B5  =  data3.CN.min()
print("\nLowest  score  in  CN  subject  From  class  B:\n") p10  =  data3[data3.CN  ==  B5]
print(p10[['Name',  'CN']].reset_index(drop=True))

plt.title("CN  Subject(Class  B)") plt.xlabel("Roll_No") plt.ylabel("Marks") p10['CN'].plot.bar()
plt.show()
else:
print("\nInvalid  Choice  !!!  Please  Enter  Class  'A'  or  'B'\n")

if  (choice  ==  '6'):
h2  =  input(str("Enter  Division  :  ")) if  (h2=='a'  or  h2=='A'):
df1  =  data.filter(["Roll_No",  'Name',  'TOC'],  axis=1) Result  =  []
for  v  in  df1['TOC']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail")

df1["Result"]  =  Result print(df1)
toc_pass  =  df1.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  TOC:",  toc_pass) roll_count1  =  df1["Roll_No"].count()
#  print(roll_count1)
per_a_toc  =  (toc_pass  /  (roll_count1))  *  100
print("Percentage  of  pass  stdents  in  TOC  of  div  A:",  per_a_toc)

labels  =  'Passed',  'Failed'  sizes  =  [per_a_toc,100-per_a_toc] colors  =  ['green',  'red']  explode  =  (0,  0)
plt.pie(sizes,  explode=explode,  labels=labels,
 
colors=colors,autopct='%1.1f%%',  shadow=True,  startangle=140) plt.axis('equal')
plt.title("TOC  Subject") plt.show()

df2  =  data.filter(["Roll_No",  'Name',  'DBMS'],  axis=1) Result  =  []
for  v  in  df2['DBMS']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail") df2["Result"]  =  Result print(df2)
dbms_pass  =  df2.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  DBMS:",  dbms_pass) roll_count2  =  df2["Roll_No"].count()
#  print(roll_count2)
per_a_dbms  =  (dbms_pass  /  (roll_count2))  *  100
print("Percentage  of  pass  stdents  in  DBMS  of  div  A:",  per_a_dbms)

labels  =  'Passed',  'Failed'
sizes1=  [per_a_dbms,  100  -  per_a_dbms] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes1,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,startangle=140)
plt.axis('equal') plt.title("DBMS  Subject") plt.show()

df3  =  data.filter(["Roll_No",  'Name',  'SEPM'],  axis=1) Result  =  []
for  v  in  df3['SEPM']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail") df3["Result"]  =  Result print(df3)
sepm_pass  =  df3.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  SEPM:",  sepm_pass) roll_count3  =  df3["Roll_No"].count() print(roll_count3)
per_a_sepm  =  (sepm_pass  /  (roll_count3))  *  100
print("Percentage  of  pass  stdents  in  SEPM  of  div  A:",  per_a_sepm)

labels  =  'Passed',  'Failed'
sizes2  =  [per_a_sepm,  100  -  per_a_sepm] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes2,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,
startangle=140) plt.axis('equal') plt.title("SEPM  Subject") plt.show()

df4  =  data.filter(["Roll_No",  'Name',  'ISEE'],  axis=1)
 
Result  =  []
for  v  in  df4['ISEE']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail") df4["Result"]  =  Result print(df4)
isee_pass  =  df4.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  ISEE:",  isee_pass) roll_count4  =  df4["Roll_No"].count()
#  print(roll_count4)
per_a_isee  =  (isee_pass  /  (roll_count4))  *  100
print("Percentage  of  pass  stdents  in  ISEE  of  div  A:",  per_a_isee)

labels  =  'Passed',  'Failed'
sizes3  =  [per_a_isee,  100  -  per_a_isee] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes3,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,
startangle=140) plt.axis('equal') plt.title("ISEE  Subject") plt.show()

df5  =  data.filter(["Roll_No",  'Name',  'CN'],  axis=1) Result  =  []
for  v  in  df5['CN']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail") df5["Result"]  =  Result print(df5)
cn_pass  =  df5.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  CN:",  cn_pass) roll_count5  =  df5["Roll_No"].count()
#  print(roll_count5)
per_a_cn  =  (cn_pass  /  (roll_count5))  *  100
print("Percentage  of  pass  stdents  in  CN  of  div  A:",  per_a_cn)

labels  =  'Passed',  'Failed'
sizes4  =  [per_a_cn,  100  -  per_a_cn] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes4,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,
startangle=140) plt.axis('equal') plt.title("CN  Subject") plt.show()

per_a_bar  =  [per_a_toc,per_a_dbms,per_a_sepm,per_a_isee,per_a_cn] sub  =  ['TOC','DBMS','SEPM','ISEE','CN']
index  =  np.arange(len(sub)) plt.bar(sub,  per_a_bar) plt.xlabel('Subject') plt.ylabel('Passing  Percentage')
 
plt.title('Passing  Percentage  Of  All  Subjects') plt.show()

elif(h2=='b'  or  h2=='B'):
df6  =  data1.filter(["Roll_No",  'Name',  'TOC'],  axis=1) Result  =  []
for  v  in  df6['TOC']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail") df6["Result"]  =  Result print(df6)
toc_pass1  =  df6.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  TOC:",  toc_pass1) roll_count6  =  df6["Roll_No"].count()
#  print(roll_count1)
per_b_toc  =  (toc_pass1  /  (roll_count6))  *  100   print("Percentage  of  pass  stdents  in  TOC  of  div  B:",  per_b_toc)

labels  =  'Passed',  'Failed'
sizes5  =  [per_b_toc,  100  -  per_b_toc] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes5,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,
startangle=140) plt.axis('equal') plt.title("TOC  Subject") plt.show()

df7  =  data1.filter(["Roll_No",  'Name',  'DBMS'],  axis=1) Result  =  []
for  v  in  df7['DBMS']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail") df7["Result"]  =  Result print(df7)
dbms_pass1  =  df7.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  DBMS:",  dbms_pass1) roll_count7  =  df7["Roll_No"].count()
#  print(roll_count2)
per_b_dbms  =  (dbms_pass1  /  (roll_count7))  *  100
print("Percentage  of  pass  stdents  in  DBMS  of  div  B:",  per_b_dbms)

labels  =  'Passed',  'Failed'
sizes6  =  [per_b_dbms,  100  -  per_b_dbms] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes6,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,
startangle=140) plt.axis('equal') plt.title("DBMS  Subject") plt.show()

df8  =  data1.filter(["Roll_No",  'Name',  'SEPM'],  axis=1)
 
Result  =  []
for  v  in  df8['SEPM']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail") df8["Result"]  =  Result print(df8)
sepm_pass1  =  df8.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  SEPM:",  sepm_pass1) roll_count8  =  df8["Roll_No"].count()
#  print(roll_count3)
per_b_sepm  =  (sepm_pass1  /  (roll_count8))  *  100
print("Percentage  of  pass  stdents  in  SEPM  of  div  B:",  per_b_sepm)

labels  =  'Passed',  'Failed'
sizes7  =  [per_b_sepm,  100  -  per_b_sepm] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes7,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,
startangle=140) plt.axis('equal') plt.title("SEPM  Subject") plt.show()

df9  =  data1.filter(["Roll_No",  'Name',  'ISEE'],  axis=1) Result  =  []
for  v  in  df9['ISEE']:
if  v  >=  12:
Result.append("Pass")
else:
Result.append("Fail") df9["Result"]  =  Result print(df9)
isee_pass1  =  df9.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  ISEE:",  isee_pass1) roll_count9  =  df9["Roll_No"].count()
#  print(roll_count4)
per_b_isee  =  (isee_pass1  /  (roll_count9))  *  100
print("Percentage  of  pass  stdents  in  ISEE  of  div  B:",  per_b_isee)

labels  =  'Passed',  'Failed'
sizes8  =  [per_b_isee,  100  -  per_b_isee] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes8,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,
startangle=140) plt.axis('equal') plt.title("ISEE  Subject") plt.show()

df10  =  data1.filter(["Roll_No",  'Name',  'CN'],  axis=1) Result  =  []
for  v  in  df10['CN']:
if  v  >=  12:
Result.append("Pass")
else:
 
Result.append("Fail") df10["Result"]  =  Result print(df10)
cn_pass1  =  df10.query('Result=="Pass"').Result.count() print("Number  of  students  passed  in  CN:",  cn_pass1) roll_count10  =  df10["Roll_No"].count()
#  print(roll_count5)
per_b_cn  =  (cn_pass1  /  (roll_count10))  *  100 print("Percentage  of  pass  stdents  in  CN  of  div  B:",  per_b_cn)

labels  =  'Passed',  'Failed'
sizes9  =  [per_b_cn,  100  -  per_b_cn] colors  =  ['green',  'red']
explode  =  (0,  0)
plt.pie(sizes9,  explode=explode,  labels=labels,  colors=colors, autopct='%1.1f%%',  shadow=True,
startangle=140) plt.axis('equal') plt.title("CN  Subject") plt.show()

per_a_bar  =  [per_b_toc,  per_b_dbms,  per_b_sepm,  per_b_isee,  per_b_cn] sub  =  ['TOC',  'DBMS',  'SEPM',  'ISEE',  'CN']
index  =  np.arange(len(sub)) plt.bar(sub,  per_a_bar) plt.xlabel('Subject') plt.ylabel('Passing  Percentage')
plt.title('Passing  Percentage  Of  All  Subjects') plt.show()

else:
print("\nInvalid  Choice  !!!  Please  Enter  Class  'A'  or  'B'\n")

if  (choice  ==  '7'):
tx  =  data2.Total.max()
print("\nHighest  scorer  From  class  A:\n") kx  =  data2[data2.Total  ==  tx]
print(kx[['Name',  'Total']].reset_index(drop=True))

tn  =  data2.Total.min()
print("\nLowest  scorer  From  class  A:\n") kn  =  data2[data2.Total  ==  tn]
print(kn[['Name',  'Total']].reset_index(drop=True))

tbx  =  data3.Total.max()
print("\nHighest  scorer  From  class  B:\n") k2  =  data3[data3.Total  ==  tbx]
print(k2[['Name',  'Total']].reset_index(drop=True))

tbn  =  data3.Total.min()
print("\nHighest  scorer  From  class  B:\n") k2n  =  data3[data3.Total  ==  tbn]
print(k2n[['Name',  'Total']].reset_index(drop=True))

#  set  width  of  bar
barWidth  =  0.25

#  set  height  of  bar
bars1  =  [tx,  tbx]
 
bars2  =  [tn,  tbn]

#  Set  position  of  bar  on  X  axis
r1  =  np.arange(len(bars1))
r2  =  [x  +  barWidth  for  x  in  r1]

#  Make  the  plot
plt.bar(r1,  bars1,  color='green',  width=barWidth,  edgecolor='white', label='Highest  Score')
plt.bar(r2,  bars2,  color='red',  width=barWidth,  edgecolor='white', label='Lowest  Score')

#  Add  xticks  on  the  middle  of  the  group  bars
plt.xlabel('Class')
plt.xticks([r  +  barWidth  for  r  in  range(len(bars1))],  ['A',  'B']) plt.ylabel('Marks')

 


ncol=1)
 
#  Create  legend  &  Show  graphic
plt.legend(loc='upper  center',  bbox_to_anchor=(1.45,  0.8),  shadow=True, plt.title('Highest  and  Lowest  Score')
plt.show()
 

if  (choice  ==  '8'):
div  =  str(input("Enter  the  Division  of  Student:  ")) n  =  int(input("Enter  the  Roll  No  of  Student  :  ")) if  (div  ==  'A'  or  div  ==  'a'):
if  n  <=  46:
print("\n\n",  data2[n  -  1:n].to_string(index=False))
else:
print("Record  Does  not  Exist!!!") elif  div  ==  'B'  or  div  ==  'b':
if  n  <=  47:
print("\n\n",  data3[n  -  1:n].to_string(index=False))
else:
print("Record  Does  not  Exist!!!")
else:
print("Record  Does  not  Exist!!!")
objects  =  ('TOC',  'DBMS',  'SEPM',  'ISEE',  'CN')
y_pos  =  np.arange(len(objects)) fig1  =  plt.figure()	#
per = []
per.insert(0,  data2['TOC'][n  -  1])
per.insert(1,  data2['DBMS'][n  -  1])
per.insert(2,  data2['SEPM'][n  -  1])
per.insert(3,  data2['ISEE'][n  -  1])
per.insert(4,  data2['CN'][n  -  1]) plt.bar(y_pos,  per,  align='center',  alpha=0.5) plt.xticks(y_pos,  objects) plt.xlabel('SUBJECTS')
plt.ylabel('MARKS') plt.title('STUDENT  GRAPH') plt.show()

p  =  inflect.engine()
space  =  p.number_to_words(n)
 
def  output(div,  n):
if  (div  ==  'A'  or  div  ==  'a'): if  n  <=  46:
print("\n\n",  data2[n  -  1:n].to_string(index=False))
else:
print("Record  Does  not  Exist!!!") elif  div  ==  'B'  or  div  ==  'b':
if  n  <=  47:
print("\n\n",  data3[n  -  1:n].to_string(index=False))
else:
print("Record  Does  not  Exist!!!")
else:
print("Record  Does  not  Exist!!!")


with  open(div  +  space  +  '.txt',  'a')  as  f:
with  contextlib.redirect_stdout(f): output(div,  n)
fig1.savefig(div  +  space  +  '_graph.pdf') if  (choice  ==  '9'):
break
