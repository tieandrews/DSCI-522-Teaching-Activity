# this prints out a list of [0,0]
foo = list(map(
    lambda a, b: a*b, [1,0], [0,1]
))
print(foo)
if __name__ == "__main__":
  implementation = 'random'
  print("")
