import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns 
# from sqlalchemy import create_engine      
from sqlalchemy import create_engine ,text

engine=create_engine(
"mysql+pymysql://mega:MEGA_CLEAN@localhost:3306/megadb",
echo=True   
)           
#TEST CONNECTION 
with engine.connect()as conn:
    result=conn.execute(text("SELECT DATABASE();"))
    print("CONNECT TO :",result.fetchone())
df=pd.read_excel(r"C:\Users\ved.katoch.DESKTOP-82LU7M3\Downloads\Mega Dataset.xlsx")
# Clean column names for MySQL
# print(df) 
# print(df.head())
# print(df.info())
# print(df.sample(10))
# df.fillna("not available",inplace=True)
df.dropna(inplace=True)
df.to_excel(r"C:\Users\ved.katoch.DESKTOP-82LU7M3\Downloads\Mega Dataset.xlsx",index=False)
# print(df.drop(columns=["Sr. No."],inplace=True))
# df.to_excel(r"C:\Users\ved.katoch.DESKTOP-82LU7M3\Downloads\Mega Dataset.xlsx",index=False)
# df.to_csv("clan data.csv",index=False)

###############################################################################
# Base Exception
# Deleting redundant columns 
# Renamina the-columns. Droppina duplicates.
# Cleanina individual columns. Remove the NaN values from the dataser
# Check for some more Transformations
############################################################################################################
# df.to_csv("clan data.csv",index=False)
print(df.rename(columns={"Unnamed_0":"S NO:"},inplace=True))

# df.to_csv("clan data.csv",index=False)
##################################################################
#### THIS IS USE TO MODIFY HIS HEADER NAME IN CALPTIAL #############
new_colum_name=[] 
for i in df.columns:
    new_colum_name.append(i.upper())
new_data_modify=df.copy()
new_data_modify.columns=new_colum_name


# print(df.head())
#################################################
##########THIS IS USE TO DROP DUPLICATE ############
print(df.duplicated().sum())
print(df.isnull().sum())# DROP NA 
#####################################################
########
df["dean_contact"] = pd.to_numeric(df["dean_contact"], errors="coerce").fillna(0).astype(int)
print(df["dean_contact"])
df["College_TPO_Contact_Number"]=pd.to_numeric(df["College_TPO_Contact_Number"],errors="coerce").fillna(0).astype(int)
print(df["College_TPO_Contact_Number"])
df["landline_no"]=pd.to_numeric(df["landline_no"] ,errors="coerce").fillna(0).astype(int)
print(df["landline_no"])
df["College_TPO_Email"]=(df["College_TPO_Email"].fillna("NA").replace(["not available","Not publicly available","not available"],"NA")) 
df.replace({"–":"NA"},inplace=True)

# df.to_csv("clean data.csv",index=False) # uoe see agin to see clean data ion csv 
# print(df.columns)
##################################################################################
############# THIS CONCEPT IS NOT POSSIBLE IN COLOUM THER R ARE MAY STR OR INT 
df['Student_Strength']=df["Student_Strength"]
print(df["Student_Strength"])
########################################################################################
df['Student_Strength']=pd.to_numeric(df["Student_Strength"],errors="coerce").fillna(0).astype(int)
print(df["Student_Strength"])
df["Student_Strength"] = df["Student_Strength"].astype(str)

df["Student_Strength"] = df["Student_Strength"].apply(
    lambda x: "2" if len(x) == 11 else x
)
df['Total_no._of_Courses']=pd.to_numeric(df["Total_no._of_Courses"],errors="coerce").fillna(0).astype(int)
print(df["Total_no._of_Courses"])

print(df.fillna("NA"))
print(df.replace({"Not Available":"NA"},inplace=True))
df.replace(["Not Available","not available","-","—","not available","Placement Cell"],"NA", inplace=True)
def clean_region(x):

    x = str(x).strip().upper()

    if x in ["NORTH", "NOTH", "NORHT", "NRTH"]:
        return "NORTH"

    elif x in ["SOUTH", "SOTH", "SUTH"]:
        return "SOUTH"

    elif x in ["EAST", "EATS", "ESAT"]: 
        return "EAST"

    elif x in ["WEST", "WSET", "WSST", "13"]:
        return "WEST"

    elif x in ["CENTRAL", "CENTARL", "CNETRAL", "NORTH CENTRAL", "NORTH-CENTRAL"]:
        return "CENTRAL"

    else:
        return None   # remove names & garbage
df["Region_North_South_East_West_Central"] = (
    df["Region_North_South_East_West_Central"].apply(clean_region).fillna("NA")
)
print(df["Region_North_South_East_West_Central"].value_counts())
df.columns = (
    df.columns
    .str.strip()                     # remove start/end spaces
    .str.replace(" ", "_", regex=False) #regex=False → treat " " as a normal space
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace(":", "", regex=False)
)

print("Cleaned columns:")
print(df.columns)

df.to_csv("clean data.csv",index=False) 

df.to_sql("MEGA_COLLAGE_DATA",con=engine,if_exists='replace',index=False)
# Sum all student strengths per region
# region_sum = df.groupby("Region_North_South_East_West_Central")["Student_Strength"].sum()
# region_sum.plot(kind="pie", autopct='%1.1f%%', figsize=(6,6))
# plt.title("Total Student Strength by Region")   
# plt.ylabel("")  # remove y-label for cleaner chart
# plt.show()


