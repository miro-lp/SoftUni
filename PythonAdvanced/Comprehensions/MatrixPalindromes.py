row, col = map(int, input().split())

print("\n".join([" ".join([chr(97 + i) + chr(97 + j + i) + chr(97 + i) for j in range(col)]) for i in range(row)]))
