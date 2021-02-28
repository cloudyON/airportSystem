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
        
        elif command == "q_":
            for i in range(3):
                print(f'{3-i} 초 후 꺼집니다.')
                time.sleep(1)

            print("\n?- program quit -y \n")
            
            break
        
