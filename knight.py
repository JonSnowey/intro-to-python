import random
mood = []

def knight():
        attitude = ['kind','stern','bold','mean']
        mood.append(random.choice(attitude))
        return random.choice(mood)
print('This knight is',knight())

def affinity():
    global mood
    return random.choice(mood)
print('This knight is still',affinity())
