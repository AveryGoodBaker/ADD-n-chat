# mylist = ['Time Management', 'Hyperactivity', 'Focus']

mydict = {
    'Time Management': 'Awesome',
    'Hyperactivity': 'Not cool',
    'Focus': '/index'
}
def Problem(problem):
    # if "Time Management" in problem:
    #     return "Take medications."
    for x in mydict:
        if x in problem:
            return mydict[x]
    # elif problem == "Time Management":
    #     return "Take medications"
    else:
        return "Is there something else that I can help you with?"



