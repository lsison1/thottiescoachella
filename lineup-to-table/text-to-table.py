with open("friday-lineup.txt", "r") as file1:
    f = file1.read()
    f2 = f.split(", ")
    for name in f2:
        print(f"<td>4</td><td>{name}</td><td>Friday</td><td>NA</td><td>NA</td></tr>")

