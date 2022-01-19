bids = {}
bidding_finished = False

def encontre_pagamento_alto (pagamento_alto):
  maisalta_oferta = 0
  winner = ""
  for bidder in maisalta_oferta:
    bid_amount = maisalta_oferta[bidder]
    if bid_amount > pagamento_alto: 
      maisalta_oferta = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${pagamento_alto}")

while not bidding_finished:
  name = input("Qual seu Nome?: ")
  price = int(input("Qual sua Oferta?: $"))
  bids[name] = price
  should_continue = input("Tem mais apostas? Digite 'Sim' ou 'Não'.\n")
  if should_continue == "Não":
    bidding_finished = True
    encontre_pagamento_alto(bids)
  elif should_continue == "Sim":
    clear()
  