import pandas
df = pandas.read_excel("C:\\Users\\KonKon\\Desktop\\csCourses.xlsx")

print (df.columns)

df.to_csv('csCourses.csv', sep=',')
