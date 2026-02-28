cardapio_completo = {
    "Comidas": {
       "Mainframe Burger": 48.0,
       "Fiber-Optic Pasta": 55.0,
       "System Crash Tacos": 38.0,
       "Circuit Board Pizza": 72.0
   },

    "Bebidas": {
      "Glitch Sour": 25.0,
      "Overclock Shot": 15.0,
      "Chrome Martini": 30.0,
      "Cyber-Cola": 10.0,
      "Data Leak": 35.0
  },

    "Sobremesas": {
      "Blue Screen Cheesecake": 28.0,
      "Neural Crunch": 12.0,
      "Kernel Brownie": 18.0,
      "Crashed'n'Creams": 24.0
  },
}

todos_produtos = {} 
for mercadoria in cardapio_completo.values(): 
    todos_produtos.update(mercadoria) 


def exibir_cardapio(lista_produtos):
    for categoria, produtos in lista_produtos.items(): 
        print(f"\n{categoria.upper()}") 
        cardapio_formatado = "\n".join([f"{produto}: {preco:.2f} créditos" for produto, preco in produtos.items()])
        print(cardapio_formatado) 


def valor_produto(lista_produtos, pedido, quantidade):
    return lista_produtos[pedido] * quantidade

def nova_tentativa_quantidade():
    tentar_novamente = input("Quer tentar inserir a quantidade novamente? (sim/não): ").strip().lower()
    return tentar_novamente in ['sim', 's']



total_conta_geral = 0.0 

print("\n" +"="*101)
print("                                     BEM VINDO (A) AO ERROR 404!                                     ")
print("="*101)
exibir_cardapio(cardapio_completo) 
print("="*101)

while True: 
    pedido = input("E aí, edgerunner, o que vai pedir? (ou digite 'sair' para encerrar): ").strip() 
    if pedido.lower() == 'sair': 
        break

    pedido_formatado = None # se usa quando ainda não tem a informação, mas quer guardar o espaço para quando tiver
    for nome_real_produto in todos_produtos.keys():
        if pedido.lower() == nome_real_produto.lower():
           pedido_formatado = nome_real_produto
           break


    if pedido_formatado: 
        print(f"Mandou bem na escolha! Processando '{pedido_formatado}'...")
        while True:
            try:
                quantidade_pedido = int(input(f"Agora me diz, quantos '{pedido_formatado}' você vai querer? "))
                
                if quantidade_pedido <= 0:
                    print("SYSTEM ERROR: A quantidade deve ser maior que zero.")
                    if not nova_tentativa_quantidade():
                        print("Pedido cancelado. Voltando ao menu principal.")
                        break
                    else:
                        continue
                    
                total = valor_produto(todos_produtos, pedido_formatado, quantidade_pedido)
                total_conta_geral += total 
                print(f"Adicionado: {quantidade_pedido}x '{pedido_formatado}'")
                print(f"Subtotal atual: {total_conta_geral:.2f} créditos.")
                break
            except ValueError:
                print("SYSTEM ERROR: Insira somente números.")
                if not nova_tentativa_quantidade():
                    print("Pedido cancelado. Voltando ao menu principal.")
                    break
                else:
                    continue
    else:
        print(f"SYSTEM ERROR: '{pedido}' não encontrado no Mainframe.")
        print("="*101)
        ver_cardapio = input("Quer dar uma olhada no cardápio novamente? (sim/não): ").strip().lower()
        if ver_cardapio in ['sim', 's']:
            exibir_cardapio(cardapio_completo)
            continue 
        else: 
            encerrar_atendimento = input("Nenhum pedido registrado. Deseja encerrar o atendimento? (sim/não): ").strip().lower()
            if encerrar_atendimento in ['sim', 's']:
                print("="*101)
                print("Beleza! Encerrando o atendimento em 3... 2... 1...\nAté a próxima, edgerunner!")
                exit()
            else:
                continue

    continuar = input("Deseja pedir algo mais? (sim/não): ").strip().lower()
    if continuar not in ['sim', 's']:
        break
   

print("\n" + "="*101)

if total_conta_geral > 0:
    print(f"TOTAL DA CONTA: {total_conta_geral:.2f} créditos")
    print("Transferência via CyberPay concluída.")
   
print("="*101)
print("Obrigado por visitar o ERROR 404!\nAté a próxima, edgerunner!")