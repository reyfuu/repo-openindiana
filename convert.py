import pandas as pd

# Read the Excel file into a dataframe
df = pd.read_excel("package openindiana/1.1.xlsx")



df['Name'] = 'pkgrecv -s http://pkg.openindiana.org/dev/ -d /audi2 pkg://openindiana.org/' + df['Name']+"@"+df["Version"]

df.drop("Version", axis=1, inplace=True)
data= df.to_string(index=False,header=False)

# data_with_text = data.replace("\n","df['Name'] = 'pkg://openindiana.org/' + df['Name']+'/'+df['Version']")

# # Write the string to a text file
with open("coba.txt", "a") as f:
        f.writelines([data])
    
