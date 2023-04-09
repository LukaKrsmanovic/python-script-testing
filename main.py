import pandas as pd
import numpy as np
import pinecone
import time


api_key = '5f6e95f3-b581-4757-a58e-04496e8d486a'
environment = 'us-east4-gcp'
index_name = 'uvod-u-masinsko-ucenje'

df = pd.read_csv('uvod-u-masinsko-ucenje_embeddings.csv')
df['embedding'] = df['embedding'].apply(eval).apply(list)

pinecone.init(api_key=api_key, environment=environment)
print('pinecone connection established')
index = pinecone.Index(index_name)
print(f'pinecone index ({index_name}) aquaried')

ind = 403871
ind_max = 579500
while ind < ind_max:
    for i in range(len(df.index)):
        df.iloc[[i], [1]] = f'{ind}'
        ind += 1
    print(f'ind je: {ind}')
    index.upsert(vectors=zip(df['id'], df['embedding']))
    print('pinecone upserted vectors')
    time.sleep(0.5)

print(f'Finished iterations, ind je {ind}')
print()
