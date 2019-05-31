SOL = 'BB'
FEEBACK = [
    """retour question 1""",
    """retour question 2""",
]

def verif(rep):
    for index, s in enumerate(SOL):
        if rep[index] == s:
            print('Bonne réponse')
        else:
            print(FEEBACK[index])