from json import load

TASKFILE = 'input.json'

# TODO решите задачу
def task() -> float:
    with open(TASKFILE) as f:
        pythfile = load(f)
    return round(sum([name['weight'] * name['score'] for name in pythfile]), 3)

print(task())
