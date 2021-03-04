

# scores's value is going to be whatever self.high_scores_list in setUp for the testfile stands for
# e.g.: [25, 120, 35, 44, 980, 325]
def latest(scores):
    return scores[-1]



def personal_best(scores):
    return max(scores)
# maybe check out the built in max() function ;)


def personal_top_three(scores):
    return sorted(scores)[-3:]
