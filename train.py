import librarian as l
import rsc.trainer as t
from tqdm import tqdm
import pandas as pd

R = 10
L = 10

print('Getting librarian..')
try:
    librarian = l.Librarian()
    names = librarian.get_names()
except:
    print('ERROR: Librarian failed to load.')
    raise

print('Getting trainer..')
try:
    trainer = t.Trainer()
except:
    print('ERROR: Trainer failed to load.')
    raise
    

print('Training...')
for name in tqdm(names*R):
    try:
        climb = librarian.get_climb(name)
        trainer.project(climb, sesh_length = L)
    except l.LibError:
        continue
    except:
        break
    
print('Saving...')
try: 
    out_path = f'wts/weights_{R}-{L}.csv'
    df = pd.DataFrame(trainer.weights, columns=None)
    df.to_csv(out_path, index=False)
    print('Training Complete!')
    print('Weights saved as', out_path)
except:
    print('ERROR: Weights could not be saved.')
    raise


