#Aardvark.library
from Aardvark import *
import re
global Regex

class Regex:
  def __init__(self, string):
    self.string=string
    self.matches={}
  def match(self, match, string=""):
    if string=="":
      string=self.string
    s=""
    num=-1
    listm=[]
    groups=[]
    finalgroups=[]
    string=self.process(string, match)
    for i in match:
      s+=i
      num+=1
      if string[num]==i:
        listm.append(True)
        continue
      if string[num]==".a":
        listm.append(True)
        continue
      if string[num].startswith("^^"):
        if not i == string[num][2:]:
          listm.append(True)
          continue
      if string[num]=="((":
        if self.match(i, string[num+1]):
          listm.append(True)
          groups.append([num, i])
        num+=1
      if string[num]=="))":
        a=groups[-1]
        groups=groups[:-1]
        finalgroups.append(a)
      else:
        print(i)
        self.matches[match]=False
        return False
      for group in groups:
        group[1]+=i
    for i in listm:
      if i!=True:
        return False
    return True, finalgroups
  def process(self, string, match):
    s=""
    fl=[]
    save=0
    for i in self.string:
      s+=i
      if s=="(":
        fl.append("((")
        s=""
      if s==")":
        fl.append("))")
        s=""
      if s=="^":
        save=1
      if s.startswith("^") and len(s)>1:
        fl.append("^"+s)
        s=""
      if s==".":
        fl.append(".a")
        s=""
      
      elif save==0 and s!="\\":
        if s.startswith("\\"):
          s=s[-1]
          
        fl.append(s)
        s=""
      if save>0:
        save-=1
    return fl
  def __repr__(self):
    return self.string


@Aardvark.type("Regex")
def RegexType(what, line_num):
  global Regex
  if type(what)==Regex:
    return True, what
  elif what.startswith("r'") and what.endswith("'"):
    return True, Regex(what[2:-1])
  elif what.startswith('r"') and what.endswith('"'):
    return True, Regex(what[2:-1])
  else:
    return False, what
    

@Aardvark.method("Regex", "match")
def RegexMatch(name, regex, match):
  return regex.match(match)