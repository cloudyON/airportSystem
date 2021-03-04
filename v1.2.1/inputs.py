import airportSystem
import time

if __name__ == "__main__":
    airportSystem.release()
    
    name = input("\n\n>>> 이름을 입력해주세요 : ")
    people = airportSystem.passenger(name)
    airport = airportSystem.airport_system()
    airline = airportSystem.airline()

    # 이스터 에그
    if name == "python":
        for i in range(100):
            print("hey! what are you doing here.. go to computer and work!! :)")

    command = ''
    print("---------------------\n\n")

    while command != 'q':
        command = input(">>> ")
        command2 = []

        if command == "reservation": # 예약
            comm = input("  - 예약하고 싶은 항공사 이름과 날짜를 입력하세요(예 : 예시항공사 3/14) : ")
            command2 = comm.split(" ")
            
            
            try :
                people.reservation(command2[0], command2[1], airline, airport)
            
            except :
                print(">>> 잘못된 항목을 넣었습니다.")
        
        
        elif command == "cancel reservation": # 예약 취소
            comm = input("  - 예약 취소하고 싶은 항공사 이름과 날짜를 입력하세요.(예 : 예시항공사 3/14)")
            command2 = comm.split(" ")

            try : 
                people.cancel_reservation(command2[0],command[1], airport)
            
            except :
                print(">>> 잘못된 항목을 넣었습니다.")
        
        elif command == "board":
            print(" - 처리 중...")
            people.board(airport)

        elif command == "check in":
            comm = input("  - 체크인하고 싶은 항공사 이름과 날짜를 입력하세요(예 : 예시항공사 3/14) : ")
            command2 = comm.split(" ")

            try :
                airport.checkIn(command2[0], command2[1], people)
            
            except :
                print(">>> 잘못된 항목을 넣었습니다.")

        elif command == "delete airline":
            comm = input("  - 지울 항공사 이름을 입력하세요 : ")

            try :
                airline.del_airline(comm)
            
            except :
                print(">>> 잘못된 항목을 넣었습니다.")

        elif command == "create airline":
            comm = input("  - 새로 만들 항공사 이름을 입력하세요 : ")

            try :
                airline.create_airlines(comm)
                
            except :
                print(">>> 잘못된 항목을 넣었습니다.")
        
        elif command == "create schedule":
            comm = input("- 항공사 이름과 새로 만들 일정을 입력하세요(예 : 예시항공사 3/15) : ")
            command2 = comm.split(" ")

            try:
                airline.create_schedule(command2[0], command[1])
            except :
                print(">>> 잘못된 항목을 넣었습니다.")

        
        
        elif command == "q_":
            for i in range(3):
                print(f'{3-i} 초 후 꺼집니다.')
                time.sleep(1)

            print("\n?- program quit -y \n")
            
            break
        
