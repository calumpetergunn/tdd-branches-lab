def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    elif final_score["home_score"] < final_score["away_score"]:
        return "Away win"
    else:
        return "Draw"
        

def get_results(final_scores):
    final_results_list = [result for result in final_scores]
    return final_results_list
        

    # (You could try and use a list comprehension for this)