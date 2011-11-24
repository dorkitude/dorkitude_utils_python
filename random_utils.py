import random

def do_weighted_draw(weights):
    total = 0;
    current_total = 0;
    bucket = 0;

    for weight in weights:
        total += weight

    rand = random.random() * total

    for weight in weights:
        current_total += weight

        if rand > current_total:
            bucket += 1
        else:
            break

    return bucket
