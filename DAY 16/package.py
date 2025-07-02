from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Pichu"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)