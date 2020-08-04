# mylist = ['Time Management', 'Hyperactivity', 'Focus']


def get_diagnosis(problem):
    mydict = {
        'Time Management': 'https://www.lifehack.org/articles/productivity/10-ways-improve-your-time-management-skills.html',
        'Managing time': "https://www.lifehack.org/articles/productivity/10-ways-improve-your-time-management-skills.html",
        'Managing my time': "https://www.lifehack.org/articles/productivity/10-ways-improve-your-time-management-skills.html",
        'managing time': "https://www.lifehack.org/articles/productivity/10-ways-improve-your-time-management-skills.html",
        'managing my time': "https://www.lifehack.org/articles/productivity/10-ways-improve-your-time-management-skills.html",
        'Hyperfocus': "https://www.additudemag.com/help-with-hyperfocus/",
        "hyperfocus": "https://www.additudemag.com/help-with-hyperfocus/",
        "Hyperfocusing": "https://www.additudemag.com/help-with-hyperfocus/",
        "hyperfocusing": "https://www.additudemag.com/help-with-hyperfocus/",
        "I am hyperfocusing": "https://www.additudemag.com/help-with-hyperfocus/",
        "I am hyperfocusing.": "https://www.additudemag.com/help-with-hyperfocus/",
        "i am hyperfocusing": "https://www.additudemag.com/help-with-hyperfocus/",
        "I can't manage my time": "https://www.lifehack.org/articles/productivity/10-ways-improve-your-time-management-skills.html",
        "I keep taking too long to do things": "https://www.lifehack.org/articles/productivity/10-ways-improve-your-time-management-skills.html",
        'Hyperactivity': "https://www.healthline.com/health/hyperactivity#:~:text=Cognitive%20behavioral%20therapy%20(CBT)%20and,hyperactivity%20and%20reduce%20its%20effects.",
        'Focus': "https://www.healthline.com/health/unable-to-concentrate",
        'focusing': "https://www.healthline.com/health/unable-to-concentrate",
        'focus': "https://www.healthline.com/health/unable-to-concentrate",
        "I can't focus.": "https://www.healthline.com/health/unable-to-concentrate",
        "I can't focus": "https://www.healthline.com/health/unable-to-concentrate",
        "I'm having trouble focusing": "https://www.healthline.com/health/unable-to-concentrate",
        "I am having a hard time focusing": "https://www.healthline.com/health/unable-to-concentrate",
        "": "Error",
        "nothing": "Great!",
        "Nothing": "Great!",
        "Nothing": "Great!",
        "I do not have a problem": "Great!"
}
    # if "Time Management" in problem:
    #     return "Take medications."
    for x in mydict:
        if x in problem:
            return {
                'problem': problem,
                'link': mydict[x]
            }
    # elif problem == "Time Management":
    #     return "Take medications"
    else:
        return "Is there something else that I can help you with?"

