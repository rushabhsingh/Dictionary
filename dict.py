import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
     
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #in case user enters words like delhi instead of Delhi
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
          U=input("Did you mean %s.  Enter Y for yes and N for no: " % get_close_matches(w,data.keys(),n=1))
          if U == "Y":
              return data[get_close_matches(w,data.keys())[0]]
          elif U =="N":
              return "It does not exist. Double check it"
          else:
              return "Sorry we did not understand your query"
    else:
        return " It does not exist"
i=0
while i<5:
        word= input("Enter the word :")
        i=i+1
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)