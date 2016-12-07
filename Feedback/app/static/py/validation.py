def feedbackValidation(feedback):
    if (len(feedback)>1200):
        return True
    else:
        return False

def satisfactionValidation(satisfaction):
    if (satisfaction == "None"):
        return True
    else:
        return False
