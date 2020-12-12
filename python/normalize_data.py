# This file normalizes the times to be in range [0,1]
import pickle

# get train and test file names
train_fname = "data/train/sr5/data_dir=grp{1..2}_npb=60000_nb=5.pkl"
test_fname = "data/test/sr5/data_dir=grp{1..2}_npb=60000_nb=5.pkl"

# open files
with open(train_fname, "rb") as f:
    train_problems = pickle.load(f)

with open(test_fname, "rb") as f:
    test_problems = pickle.load(f)

# get current times
times = []
for problem in train_problems:
    print(problem.is_time)
    times.extend(problem.is_time)
for problem in test_problems:
    print(problem.is_time)
    times.extend(problem.is_time)

# compute min, max, range of times
min, max = min(times), max(times)
range = max - min
print(f"statistics for this data: min solver time is {min}s and max time is {max}s")

# update all times to (current_time - min)/(max - min)
for problem in train_problems:
    for time in problem.is_time:
        time = (time-min)/range

for problem in test_problems:
    for time in problem.is_time:
        time = (time-min)/range

# save updated times back to the same file
with open(train_fname, 'wb') as f_dump:
    pickle.dump(train_problems, f_dump, protocol=0)

with open(test_fname, 'wb') as f_dump:
    pickle.dump(test_problems, f_dump, protocol=0)