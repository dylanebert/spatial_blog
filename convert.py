import pandas as pd
import seaborn as sns
import json

df = pd.read_csv('data.csv', sep='\t', header=None, names=['frame', 'posX', 'posY', 'posZ', 'rotX', 'rotY', 'rotZ', 'rotW'])
df.set_index('frame', drop=True, inplace=True)
labels = ['posX', 'posY', 'posZ']
z = df[labels].to_numpy()
n_frames, n_dim = z.shape
pal = sns.color_palette('hls', n_dim).as_hex()
datasets = []
for i in range(n_dim):
    points = []
    for j in range(n_frames):
        point = float(z[j, i])
        points.append(point)
    dataset = {
        'data': points,
        'label': labels[i],
        'borderColor': pal[i],
        'fill': False
    }
    datasets.append(dataset)
data = {'labels': df.index.to_numpy().astype(str).tolist(), 'datasets': datasets}
with open('data.json', 'w+') as f:
    json.dump(data, f)
