def collect_information() -> dict:
    information = {}
    with open("data/measurements_1k.txt", encoding= "utf-8") as f:

        for line in f:
            line = line.rstrip("\n")
            station, semicolon, temperature=line.partition(";")
            temperature= float(temperature)


            if station not in information :
                information[station]=[temperature, temperature, 1, temperature]
            else:
                inf_of_station = information[station]


                inf_of_station[1]+=temperature
                inf_of_station[2]+=1
                if inf_of_station[0]> temperature:
                    inf_of_station[0]=temperature
                if inf_of_station[3]<temperature:
                    inf_of_station[3]=temperature

    return information

def print_information(information:dict) -> None:
        for station in sorted(information):
            inf_of_station=information[station];
            mean = inf_of_station[1]/inf_of_station[2]
            print(f"{station};{inf_of_station[0]:.1f};{mean:.1f};{inf_of_station[3]:.1f}")

if __name__ == "__main__":

    print_information(collect_information())