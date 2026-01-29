try:
    fh =open("sample.txt", "r")
    line1 = fh.readline()
    line2 = fh.readline()
    print("Reading file content:")
    print(f"line 1: {line1}".strip())
    print(f"line 2: {line2}")

    fh.close()
except FileNotFoundError:
    print("The file sample.txt was not found.")