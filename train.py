import librarian as l
import rsc.trainer as t
import rsc.progress_bar as pb
import csv
from numpy import mean
import sys
from termcolor import colored
import os

os.system('color')

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
        pbar = pb.Pb(names[:10], f'Session {r}:')
        scores = []
        max_score = 0
        worst_name = ''
        for name in pbar:
            try:
                climb = librarian.get_climb(name)
                score = trainer.project(climb, sesh_length = L)
                scores += [score]
                if score>max_score:
                    max_score = score
                    worst_name = name
                if len(name) >= 10:
                    name = name[:10]
                else:
                    name += ' ' * (10 - len(name))
                pbar.suff = f'{name} <= {colored(round(max_score,3),"red")}'
            except l.LibError:
                continue
            except:
                raise
        pbar.complete(colored(f'Session {r}: ','green') + colored(round(mean(scores),3),'yellow') + f' <= {colored(round(max_score,3),"red")} on {worst_name}')
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


