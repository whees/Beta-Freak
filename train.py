import librarian as l
import rsc.trainer as t
from tqdm import tqdm 
import csv
from numpy import mean
import sys

try:
    R = int(sys.argv[0])
    L = int(sys.argv[1])
except:
    R = 10
    L = 10

print('Getting librarian..')
try:
    librarian = l.Librarian()
    names = librarian.get_names()
except:
    print('ERROR: Librarian failed to load.')
    raise

print('Getting trainer...')
try:
    trainer = t.Trainer()
except:
    print('ERROR: Trainer failed to load.')
    raise

print('Training...') 
for r in range(R):
    try:
        pbar = tqdm(names)
        scores = []
        for name in pbar:
            try:
                climb = librarian.get_climb(name)
                scores += [trainer.project(climb, sesh_length = L)]
                pbar.set_description(f'Session {r}')
            except l.LibError:
                continue
            except:
                raise
        print('Average score:', round(mean(scores),3))
    except:
        break
        
    
print('\nSaving...')
try: 
    out_path = f'wts/weights_{R}-{L}.csv'
    with open(out_path, 'w') as out_file:
        wr = csv.writer(out_file)
        wr.writerow(trainer.weights)
    print('Training Complete!')
    print('Weights saved as', out_path)
except:
    print('ERROR: Weights could not be saved.')
    raise


