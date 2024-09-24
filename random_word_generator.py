import random
words = {}



def main():
    random_choice = random_word()
    desired = input("Which parts of speech do you want?\nLeave blank for random\n")
    PARTS_OF_SPEECH = ("verb", "noun", "pronoun", "adjective", "adverb", "preposition", "conjunction", "interjection")
    while ("and " in desired and "not " in desired) or ("and " in desired and "or " in desired) or ("or " in desired and "not "in desired):
        print("Error: cannot have two operators at once")
        desired = input("Which parts of speech do you want?\nLeave blank for random\n")
    if desired == "e":
        exit()
    elif desired == '':
        output(desired, random_choice, PARTS_OF_SPEECH)
        return
    elif "or" in desired:
        desired = desired.replace(" ", "").split("or")
        if has_valid_parts(desired, PARTS_OF_SPEECH):
            output([or_operator(desired)], random_choice, PARTS_OF_SPEECH)
        else:
            print("Invalid parts of speech, try again")
    elif "not" in desired:
        desired = desired.replace(" ", "").split("not")
        if '' in desired:
            desired.remove('')
        if has_valid_parts(desired, PARTS_OF_SPEECH):
            output([not_operator(desired, PARTS_OF_SPEECH)], random_choice, PARTS_OF_SPEECH)
            return
        else: 
            print("Invalid parts of speech, try again")
            main()
    elif "and" in desired:
        desired = desired.replace(" ", "").split("and")
        if has_valid_parts(desired, PARTS_OF_SPEECH):
            output(desired, random_choice, PARTS_OF_SPEECH)
            return
        else: 
            print("Invalid parts of speech, try again")
            main()
    else:
        desired = [desired]
        if has_valid_parts(desired, PARTS_OF_SPEECH):
            output(desired, random_choice, PARTS_OF_SPEECH)
        else:
            print("invalid part of speech, try again")
            main()
        


    #verb v. 
    #noun n. 
    #pronoun pron. 
    #adjective adj. 
    #adverb adv. 
    #preposition prep. 
    #conjunction conj. 
    #interjection int. 



def dictionize():
    '''
    Turns the oxford dictionary into a python dictionary with "word":{part of speech}
    Returns list
    '''
    with open("dictionary.txt", 'r', encoding='utf8') as dictionary:
        for i in dictionary:
            x = 0
            if i != '\n':
                wordAndDef = i.lower().split("  ")
                try: #try here because not every line has a "  ", will cause IndexError
                    #TODO: fix so only lines with "  " go into here
                    for ii in wordAndDef[1]:
                        if ii == ' ':
                            break
                        x += 1
                    words[wordAndDef[0]] = wordAndDef[1][0:x]
                    if not(words[wordAndDef[0]].isalpha()):
                        words[wordAndDef[0]] = words[wordAndDef[0].rstrip()]
                except IndexError:
                    continue
    return words



class random_word:
    def __init__(self):
        self.partOfSpeechSearchList = []
        
    def verb(self, words):
        """
        Searches for verbs in the dictionary of word:(part of speech) pairs

        words:dicionary
        """
        for i in words:
            if ("v." in words[i]) and ("adv." not in words[i]):
                self.partOfSpeechSearchList.append(i)
        return self.partOfSpeechSearchList[random.randint(0, len(self.partOfSpeechSearchList))]
                
    def noun(self, words):
        """
        Searches for nouns in the dictionary of word:(part of speech) pairs

        words:dicionary, words and parts of speech pairs
        """
        for i in words:
            if ("n." in words[i]) and ("on." not in words[i]):
                self.partOfSpeechSearchList.append(i)
        return self.partOfSpeechSearchList[random.randint(0, len(self.partOfSpeechSearchList))]

    def adjective(self, words):
        """
        Searches for adjectives in the dictionary of word:(part of speech) pairs

        words:dicionary, words and parts of speech pairs
        """
        for i in words:
            if ("adj." in words[i]):
                self.partOfSpeechSearchList.append(i)
        return self.partOfSpeechSearchList[random.randint(0, len(self.partOfSpeechSearchList))]
    
    def pronoun(self, words):
        """
        Searches for pronouns in the dictionary of word:(part of speech) pairs

        words:dicionary, words and parts of speech pairs
        """
        for i in words:
            if ("pron." in words[i]):
                self.partOfSpeechSearchList.append(i)
        return self.partOfSpeechSearchList[random.randint(0, len(self.partOfSpeechSearchList))]
    
    def adverb(self, words):
        """
        Searches for adverbs in the dictionary of word:(part of speech) pairs

        words:dicionary, words and parts of speech pairs
        """
        for i in words:
            if ("adv." in words[i]):
                self.partOfSpeechSearchList.append(i)
        return self.partOfSpeechSearchList[random.randint(0, len(self.partOfSpeechSearchList))]
    
    def preposition(self, words):
        """
        Searches for prepositions in the dictionary of word:(part of speech) pairs

        words:dicionary, words and parts of speech pairs
        """
        for i in words:
            if ("prep." in words[i]):
                self.partOfSpeechSearchList.append(i)
        return self.partOfSpeechSearchList[random.randint(0, len(self.partOfSpeechSearchList))]
    
    def conjunction(self, words):
        """
        Searches for conjunctions in the dictionary of word:(part of speech) pairs

        words:dicionary, words and parts of speech pairs
        """
        for i in words:
            if ("conj." in words[i]):
                self.partOfSpeechSearchList.append(i)
        return self.partOfSpeechSearchList[random.randint(0, len(self.partOfSpeechSearchList))]
    
    def interjection(self, words):
        """
        Searches for interjections in the dictionary of word:(part of speech) pairs

        words:dicionary
        """
        for i in words:
            if ("int." in words[i]):
                self.partOfSpeechSearchList.append(i)
        return self.partOfSpeechSearchList[random.randint(0, len(self.partOfSpeechSearchList))]

    #verb v. done
    #noun n. done
    #pronoun pron. done
    #adjective adj. done
    #adverb adv. done
    #preposition prep. done
    #conjunction conj. done
    #interjection int. done



def has_valid_parts(desired, PARTS_OF_SPEECH):
    """
    Checks if desired contains exact parts of speech or misspelt ones
    Returns True or False

    desired: list
    PARTS_OF_SPEECH: list or tuple
    """
    for x in desired:
            coincidence = False
            for y in PARTS_OF_SPEECH:
                if x == y:
                    coincidence = True
                    break
            if not coincidence:
                return False
    return True



def not_operator(desired, PARTS_OF_SPEECH):
    """
    Returns a random choice from a list of items that are not excluded

    desired: list
    PARTS_OF_SPEECH: list or tuple
    """
    withoutExcluded = list(PARTS_OF_SPEECH)
    for x in desired:
        withoutExcluded.remove(x)
    return random.choice(withoutExcluded)



def or_operator(desired):
    return random.choice(desired)



def output(desired, random_choice, PARTS_OF_SPEECH):
    if desired == '':
        desired = [random.choice(PARTS_OF_SPEECH)]
    for x in desired:
            match x:
                case "verb":
                    print(random_choice.verb(words))
                case "noun":
                    print(random_choice.noun(words))
                case "pronoun":
                    print(random_choice.pronoun(words))
                case "adjective":
                    print(random_choice.adjective(words))
                case "adverb":
                    print(random_choice.adverb(words))
                case "preposition":
                    print(random_choice.preposition(words))
                case "conjunction":
                    print(random_choice.conjunction(words))
                case "interjection":
                    print(random_choice.interjection(words))
                case _: 
                    print(f"{x} is not a valid part of speech (this shouldn't be possible)")
            random_choice.partOfSpeechSearchList.clear()


if __name__ == "__main__":
    words = dictionize()
    exit_ = ''
    while exit_ != 'e':
        print("Press e to exit")
        main()
        exit_ = input()


