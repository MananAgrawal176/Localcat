import pandas as pd

df= pd.DataFrame({
    'Name' : ['Aarav', 'Ishita','Rohan','Tanvi','Karan','Sneha','Vihaan','Ananya','Kabir','Pooja'],
    'Subject' : ['Math' , 'English' , 'Hindi' , 'Math' , 'English' , 'Social Science' , 'Math' , 'English' , 'Science' , 'Math' ],
    'Score' : [55,76,98,77,67,87,69,92,54,74],
    'Grade' : [None]*10
})
print(df)
# Part 1
df['Grade']= ['A' if num>= 90 else
             'B' if num>=80 else
             'C' if num>=70 else
             'D' if num>=60 else
             'F'  
             for num in df['Score']]
print(df)

# Part 2
df_new = df.sort_values('Score', ascending= False)            
print (df_new.to_string(index= False))

# Part 3
grouped= df.groupby('Subject')['Score'].mean().round(2)
print (grouped)

# Part 4
def pandas_filter_pass(df):
#.isin return bool value ans df[] select row which has truth value= True and df['Grade'] select the column
   df1=  df[df['Grade'].isin(['A', 'B']) ]
   return df1
        
print(pandas_filter_pass(df))