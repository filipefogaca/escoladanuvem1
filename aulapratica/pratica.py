print("olá filipe, seja bem vindo !")
status = input("você esta bem?")

status = input("você esta bem? (s/n): ")
if status == "s":
  print("que bon, fico feliz!")
elif status == "n":
  print("sinto muito, melhoras.")
else:
  print("tente novamente com (s/n)")
