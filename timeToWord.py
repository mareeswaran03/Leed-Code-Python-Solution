hours=5
minutes=28
def timeinWords(hours,minutes):
    hourinString={
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine",
        10:"Ten",
        11:"Eleven",
        12:"Twelve"
    }
    minuteinString={
        0:"of dock",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine",
        10:"Ten",
        11:"Eleven",
        12:"Twelve",
        13:"Thirteen",
        14:"Fourteen",
        15:"Quater",
        16:"Sixteen",
        17:"Seventeen",
        18:"Eighteen",
        19:"Ninteen",
        20:"Twenty",
        30:"half",
        45:"Quater"
    }

    if minutes==0:
        return hourinString[hours]+" "+minuteinString[minutes]
    elif minutes==1:
        return minuteinString[minutes]+" minute past "+hourinString[hours]
    elif minutes<40:
        if minutes==15 or minutes==30:
            return minuteinString[minutes]+" past "+hourinString[hours]
        elif minutes>20 and minutes<30:
            secmin=minutes-20
            minutes-=secmin
            return minuteinString[minutes]+"-"+minuteinString[secmin]+" minutes past "+hourinString[hours]
        elif minutes>30 and minutes<40:
            secmin=minutes-30
            return "Thirty-"+minuteinString[secmin]+" minutes past "+hourinString[hours]
    elif minutes>=40:
        if minutes==45:
            hours+=1
            return minuteinString[minutes]+" to "+hourinString[hours]
        else:
            minutes=60-minutes
            hours+=1
            return minuteinString[minutes]+" minutes past to "+hourinString[hours]
    

print(timeinWords(hours,minutes))

        
