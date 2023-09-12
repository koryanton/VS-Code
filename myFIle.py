n = int(input("Check this number: "))


def prime_checker(number=n):
  myList = []
  for number in range(2, n):
      myList.append(n % number)
  if 0 in myList:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")
  return myList


prime_checker(n)
