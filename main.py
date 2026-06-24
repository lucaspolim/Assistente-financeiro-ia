print("=== Assistente Financeiro Inteligente ===")

nome = input("Digite seu nome: ")

contexto = {
    "nome": nome,
    "ultimo_valor": None,
    "ultima_taxa": None,
    "ultimo_tempo": None,
    "historico": []
}

def responder_faq(pergunta):
    if "pix" in pergunta:
        return "PIX é uma forma de pagamento instantânea, disponível todos os dias, a qualquer horário."
    elif "cartão" in pergunta or "cartao" in pergunta:
        return "O cartão permite compras à vista ou parceladas. É importante acompanhar limite, vencimento e fatura."
    elif "empréstimo" in pergunta or "emprestimo" in pergunta:
        return "Empréstimo é um valor liberado pelo banco que deve ser pago com juros em parcelas."
    elif "investimento" in pergunta or "investir" in pergunta:
        return "Investimento é uma forma de aplicar dinheiro buscando rendimento ao longo do tempo."
    elif "segurança" in pergunta or "seguranca" in pergunta or "golpe" in pergunta:
        return "Nunca compartilhe senhas, códigos de verificação ou dados bancários por mensagem."
    else:
        return "Não encontrei uma resposta exata, mas posso ajudar com PIX, cartão, empréstimo, investimento e segurança."

def simular_investimento():
    valor = float(input("Valor para investir: "))
    taxa = float(input("Taxa de rendimento (%): "))
    tempo = float(input("Tempo em anos: "))

    rendimento = valor * (taxa / 100) * tempo
    total = valor + rendimento

    contexto["ultimo_valor"] = valor
    contexto["ultima_taxa"] = taxa
    contexto["ultimo_tempo"] = tempo

    return f"Com investimento de R$ {valor:.2f}, taxa de {taxa:.2f}% ao ano por {tempo:.1f} ano(s), o rendimento estimado é de R$ {rendimento:.2f}. Total final: R$ {total:.2f}."

def simular_emprestimo():
    valor = float(input("Valor do empréstimo: "))
    taxa = float(input("Taxa de juros mensal (%): "))
    parcelas = int(input("Quantidade de parcelas: "))

    juros_total = valor * (taxa / 100) * parcelas
    total = valor + juros_total
    parcela = total / parcelas

    contexto["ultimo_valor"] = valor
    contexto["ultima_taxa"] = taxa
    contexto["ultimo_tempo"] = parcelas

    return f"Para um empréstimo de R$ {valor:.2f}, com taxa de {taxa:.2f}% ao mês em {parcelas} parcelas, o total estimado será R$ {total:.2f}. Cada parcela será aproximadamente R$ {parcela:.2f}."

def responder_com_contexto(pergunta):
    if "mesma taxa" in pergunta or "mesmo rendimento" in pergunta:
        if contexto["ultima_taxa"] is not None:
            novo_valor = float(input("Informe o novo valor: "))
            taxa = contexto["ultima_taxa"]
            tempo = contexto["ultimo_tempo"]

            rendimento = novo_valor * (taxa / 100) * tempo
            total = novo_valor + rendimento

            return f"Usando a mesma taxa de {taxa:.2f}% e o mesmo período informado antes, o rendimento estimado será R$ {rendimento:.2f}. Total final: R$ {total:.2f}."
        else:
            return "Ainda não existe uma taxa anterior salva no contexto."

    return responder_faq(pergunta)

while True:
    print("\nComo posso ajudar?")
    print("1 - Fazer pergunta financeira")
    print("2 - Simular investimento")
    print("3 - Simular empréstimo")
    print("4 - Ver histórico")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pergunta = input("Digite sua pergunta: ").lower()
        contexto["historico"].append(pergunta)

        resposta = responder_com_contexto(pergunta)
        print(f"\n{nome}, {resposta}")

    elif opcao == "2":
        resposta = simular_investimento()
        contexto["historico"].append("Simulação de investimento")
        print(f"\n{nome}, {resposta}")

    elif opcao == "3":
        resposta = simular_emprestimo()
        contexto["historico"].append("Simulação de empréstimo")
        print(f"\n{nome}, {resposta}")

    elif opcao == "4":
        print("\nHistórico da conversa:")
        if len(contexto["historico"]) == 0:
            print("Nenhuma interação registrada.")
        else:
            for item in contexto["historico"]:
                print("-", item)

    elif opcao == "5":
        print(f"Atendimento encerrado. Obrigado, {nome}!")
        break

    else:
        print("Opção inválida. Tente novamente.")
