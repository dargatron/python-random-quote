import random
last = 13
rnd = random.randint(0, last)
def minor():
   # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  minor()
