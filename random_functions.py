import random
def common_dist(insanitylevel):
    return (random.randint(1, 5)<insanitylevel or insanitylevel >= 10)

def normal_dist(insanitylevel):
    return (random.randint(1, 10)<insanitylevel or insanitylevel >= 10)

def uncommon_dist(insanitylevel):
    return (random.randint(1, 18)<insanitylevel or insanitylevel >= 10)

def rare_dist(insanitylevel):
    roll = (random.randint(1, 30)<insanitylevel or insanitylevel >= 11)
    if(roll):
        print("adding something rare to the prompt")
    return roll

def legendary_dist(insanitylevel):
        roll = (random.randint(1, 50)<insanitylevel)
        if(roll):
            print("Nice! adding something legendary to the prompt")
        return roll

def unique_dist(insanitylevel):
        roll = (random.randint(1, 75)<insanitylevel)
        if(roll):
            print("Critical hit! Something unique has been added to the prompt")
        return roll

def novel_dist(insanitylevel):
        roll = (random.randint(1, 500)<insanitylevel)
        if(roll):
            print("Uh, something novel has been added to the prompt. Interesting.")
        return roll