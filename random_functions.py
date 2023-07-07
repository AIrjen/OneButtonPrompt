import random
def common_dist(insanitylevel):
    return (random.randint(1, 5)<insanitylevel or insanitylevel >= 10)

def normal_dist(insanitylevel):
    return (random.randint(1, 10)<insanitylevel or insanitylevel >= 10)

def uncommon_dist(insanitylevel):
    return (random.randint(1, 18)<insanitylevel or insanitylevel >= 10)

def rare_dist(insanitylevel):
    roll = (random.randint(1, 30)<insanitylevel or insanitylevel >= 10)
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

def extraordinary_dist(insanitylevel):
        roll = (random.randint(1, 200)<insanitylevel)
        if(roll):
            print("Extraordinary! Something special has been added to the prompt")
        return roll

def novel_dist(insanitylevel):
        roll = (random.randint(1, 500)<insanitylevel)
        if(roll):
            print("Uh, something novel has been added to the prompt. Interesting.")
        return roll


def chance_roll(insanitylevel, chance):
    chance_mapping = {
        'never': {'set_number': 0, 'message': ""},
        'novel': {'set_number': 500, 'message': "Uh, something novel has been added to the prompt. Interesting."},
        'extraordinary': {'set_number': 200, 'message': "Extraordinary! Something special has been added to the prompt"},
        'unique': {'set_number': 75, 'message': "Critical hit! Something unique has been added to the prompt"},
        'legendary': {'set_number': 50, 'message': "Nice! adding something legendary to the prompt"},
        'rare': {'set_number': 30, 'message': "adding something rare to the prompt"},
        'uncommon': {'set_number': 18, 'message': ""},
        'normal': {'set_number': 10, 'message': ""},
        'common': {'set_number': 5, 'message': ""},
        'always': {'set_number': 1, 'message': ""},
    }
    if chance == 'never':
        return False
    if chance in chance_mapping:
        properties = chance_mapping[chance]
        set_number = properties['set_number']
        message = properties['message']
        # if we have insanity level of 10, then every under rare is alwas true
        if (set_number <= 35 and insanitylevel >= 10):
            if(message != ""):
                print(message)
            return True 
        roll = random.randint(1, set_number) < insanitylevel
        if(message != "" and roll == True):
                print(message)
        return roll
    else:
        raise ValueError(f"Invalid chance value: {chance}")
