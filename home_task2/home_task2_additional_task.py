from tqdm import tqdm
import time

# adding loading bar to console

for i in tqdm([1, 2, 3, 4, 5], desc ="Loading..."):
    time.sleep(0.3)

