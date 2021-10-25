import boto3
import pandas as pd

from io import StringIO

client = boto3.client('s3')
    
csv_obj = client.get_object(Bucket='veenasbucket', Key='movies.csv')

#print(csv_obj['Body'])

csv_obj_body = csv_obj['Body']

csv_string = csv_obj_body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))

#To print the number of rows in the head
print(df.head(10))

#Filtering through romance genre
df_romance = df[df.Genre=='Romance']

#Printing the head and size of the data
#print(df_romance.head())
#print(df_romance.shape)

#Printing two columns from the dataframe
print(df_romance[['Film', 'Year']])


