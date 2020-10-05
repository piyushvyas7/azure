import re

COPYRIGHT = "\u00A9" #©
MAPPING_TABLE = {
    # © will also work but to be consistent and less mantainability using a variable
    #"Oracle" : "Oracle©",
    "Oracle" : "Oracle©",
    "Google" : "Google"+COPYRIGHT,
    "Microsoft" : "Microsoft"+COPYRIGHT,
    "Amazon" : "Amazon"+COPYRIGHT,
    "Deloitte" : "Deloitte"+COPYRIGHT
}


def replaceAll(stringToReplace):
    for i, j in MAPPING_TABLE.items():
        stringToReplace = re.sub('(\\b' + i + '\\b)',str(j), stringToReplace)
    return stringToReplace


# this function was working for most of the cases but it was not able to handle a special scenario
# e.g. {hell} and [hello] or {hell,} { hell. } are two different words... when I am playing to replace hell with heaven
# it should replace only {hell} and not [hell]o .. i.e it should not make [heaven]o
#


#def replaceAll(stringToReplace):
#    newstring = []
#    for word in stringToReplace.split(' '):
#        if word in MAPPING_TABLE:
#            newstring.append(word.replace(word, MAPPING_TABLE[word]))
#        else:
#            newstring.append(word)
#    return (' ').join(newstring)