import sys
def collect_information(file_path: str) -> dict:
    information = {}
    with open(file_path, "rb") as f:

        for line in f:
            line = line.rstrip(b"\n\r")
            station_bytes, semicolon, temperature_bytes=line.partition(b";")
            temperature= float(temperature_bytes)
            if station_bytes not in information :
                information[station_bytes]=[temperature, temperature, 1, temperature]
            else:
                inf_of_station = information[station_bytes]
                inf_of_station[1]+=temperature
                inf_of_station[2]+=1
                if inf_of_station[0]> temperature:
                    inf_of_station[0]=temperature
                if inf_of_station[3]<temperature:
                    inf_of_station[3]=temperature
    return information

def print_information(information:dict) -> None:
        for station_bytes in sorted(information, key = lambda x: x.decode("utf-8")):
            inf_of_station=information[station_bytes]
            mean = inf_of_station[1]/inf_of_station[2]
            station = station_bytes.decode("utf-8")
            print(f"{station};{inf_of_station[0]:.1f};{mean:.1f};{inf_of_station[3]:.1f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ошибка: файл не передан", file=sys.stderr)
        sys.exit(1)
    else:
        try:
            file_path=sys.argv[1]
            print_information(collect_information(file_path))
        except FileNotFoundError:
            print("Ошибка: файл не найден", file=sys.stderr)
            sys.exit(1)