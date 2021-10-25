import boto3
import pandas as pd

from io import StringIO

client = boto3.client('s3')

#Accessing the file from the bucket
csv_obj = client.get_object(Bucket='veenasbucket', Key='movies.csv')

#Storing the body of the object in a variable
csv_obj_body = csv_obj['Body']

#Decoding the data in the body... utf-8 is a standard string format
csv_string = csv_obj_body.read().decode('utf-8')

#Creating a dataframe
df = pd.read_csv(StringIO(csv_string))

#Filtering and creating a df comedy
df_comedy = df[df.Genre=='Comedy']

# Write the filtered data into S3
csv_buf = StringIO()
df_comedy.to_csv(csv_buf, header=True, index=False)
csv_buf.seek(0)
client.put_object(Bucket='veenasbucket', Body=csv_buf.getvalue(), Key='movies_comedy.csv')