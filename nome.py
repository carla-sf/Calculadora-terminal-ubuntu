while True:
  num1 = float(input("Digite o primeiro número:"))
  num2 = float(input("Digite o segundo número"))

  print("Escolha a operação desejada:")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")

  opcao = input("Digite o número correspondente a operação desejada:")

  if opcao == "1":
    resultado = num1 + num2
    print("O resultado da soma é:" , resultado)
  elif opcao == "2":
      resultado = num1 - num2
      print("O resultado da subtração é:" , resultado)
  elif opcao == "3":
    resultado = num1 * num2
    print("O resultado da multiplicação é:" , resultado)
  elif opcao == "4":
    resultado = num1 / num2
    print("O resultado da divisão é:" , resultado)
  else:
    print("Opção não existe!")

