from tqdm import tqdm
import time

for i in tqdm([1, 2, 3, 4, 5], desc ="Loading..."):
    time.sleep(0.3)

