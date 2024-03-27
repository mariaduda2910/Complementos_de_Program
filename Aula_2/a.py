elif op == 3:  # Salvar Pessoas 
with open("list_of_colors.pkl", "wb") as f:
    pickle.dump(list_of_colors, f)
elif op == 4:  # Carregar Pessoas
with open("list_of_colors.pkl", "rb") as f:
    list_of_colors = pickle.load(f)