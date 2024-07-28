while True:
  import random
  
  letter = ['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']
  
  rand1 = letter[random.randint(0,25)]
  rand2 = letter[random.randint(0,25)]
  rand3 = letter[random.randint(0,25)]
  rand4 = letter[random.randint(0,25)]
  rand5 = letter[random.randint(0,25)]
  rand6 = letter[random.randint(0,25)]
  
  print("\n<==> WELCOMME TO SIMULATION WORLD AND SECRET CODE WORLD <==> \n")
  gen = input("\n\n If You Want To Generate Code Then Press G or You Want To Decode The Secret Code Into General Word Then Press D :: (G/D) ::==> ")
  
  
  if(gen == 'G' or gen == 'g'):
      print("\n<==========WANT TO GENERATE YOUR  PRIVATE MESSAGE===========>\n")
      a = input(" enter Your code::")
      a1 = a.split()
      # b = len(a)
      newSent = ""
      for i in a1:
        if (len(i)<=2):
  
            def reverse (n):
                str=""
                for i in n:
                    str = i+ str
  
                return str
            final1 = reverse(i)
            newSent = newSent + final1 + " "
        else:
  
            def reverseAgain(n):
               n1 = n[0]
               # print(n1)
               firstW = (n1[0])
               d = n.removeprefix(n1[0])
               e = d + firstW
               f = rand1 +rand2 + rand3 + e + rand4 + rand5 + rand6
               return f
  
            final = reverseAgain(i)
            newSent = newSent + final+ " "
  
      print("Your Secret Code is Ready ==> ", newSent.strip())
  
  elif(gen == 'D' or gen == 'd'):
      print("\n<==========WANT TO KNOW YOUR FRIEND PRIVATE MESSAGE===========>\n")
  
      msg = input("Enter your friend's message: ")
      msg1 = msg.split()
      decodeStr = ""
  
      # Define functions outside the loop
      def reverse(n):
          str = ""
          for p in n:
              str = p + str
          return str
  
      def reverseAgain(n):
          d = n[3:-3]  # Assuming you want to remove first 3 and last 3 characters
  
          e = d[-1]
          f = d.rstrip(d[-1])
          g = e + f
          return g
  
  
      # Process each word in the message
      for i in msg1:
          if len(i) < 3:
              result = reverse(i)
              decodeStr += result + " "
          else:
              result1 = reverseAgain(i)
              decodeStr += result1 + " "
  
      print("Your Secret Code is Ready ==> ", decodeStr)
  
  else:
      print("you are out of program ")