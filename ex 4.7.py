def computegrade():
    score = input('score\n')
    try:
        score = float(score)
    except ValueError:
        print('bad score')
        quit()
    if score > 1:
        print('bad score')
        quit()
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score <= 0.6:
        print('F')
    else:
        print('bad score')
    return score


computegrade()
