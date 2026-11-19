def read_file():
    with open("data/measurements_1k.txt", encoding= "utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            station, semicolon, temperature=line.partition(";")
            temperature= float(temperature)
            print(station, temperature)


if __name__ == "__main__":
    read_file()