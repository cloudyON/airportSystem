import time

class passenger():
    def __init__(self, names):
        self.money = 0
        self.schedule = 0
        self.name = names    

    def reservation(self, air:'nameofAirline', date ,airline:'clsAl', airport_system:'clsAs'):
        slash = 0
        
        if '/' in date:
            slash = date.index('/')
            
            if air in airline.airlines and date in airline.all_Schedule[air] and 12 >= int(date[0:slash]) >= 1 and 31 >= int(date[(slash+1):len(date)]) >= 1: # 날짜에서 슬래시 위치를 찾은 다음 인덱싱을 이용하여 제대로된 것인지 검사.
                agree = input("예약을 하시겠습니까? (y/n)")
                
                if agree == 'y':
                   
                    if self.name not in airport_system.airScheduleAIR: # 만약 처음 예약이라면 자기 이름 : [] dict 만들기
                        airport_system.airScheduleAIR[self.name] = []
                        airport_system.airScheduleDATE[self.name] = []

                    airport_system.airScheduleAIR[self.name].append(air)
                    airport_system.airScheduleDATE[self.name].append(date)

                    print("\n-------airportSystem-------")
                    print(f"{date} 날짜에 {air}항공사에 등록되었습니다.")
                    print("\n--------------\n")
                else :
                    print("\n-------airportSystem-------\n 예약이 취소되었습니다. \n --------------\n")

            else:
                print("일정이 존재하지 않거나 항공사가 잘못 입력되었습니다.")

        else:
            print("날짜를 잘못입력하셨습니다.")
    
    def cancel_reservation(self,air:'airline name', date:'date of reservation',airport_systems : 'clsAS'):
        if self.name in (airport_systems.airScheduleAIR and airport_systems.airScheduleDATE):
            
            if air in airport_systems.airScheduleAIR[self.name] and date in airport_systems.airScheduleDATE[self.name]:
                answer = input("정말로 취소하시겠습니까? (y/n) ")
                
                if answer == "y":
                    airport_systems.airScheduleAIR[self.name].remove(air)
                    airport_systems.airScheduleDATE[self.name].remove(date)

                    print("\n-------airportSystem-------\n\n제거가 완료되었습니다.\n\n--------------\n")
                else :
                    print('-------예약 취소가 취소되었습니다.-------')
    
            else :
                print("예약 취소할 항목이 없습니다.")
        
        else :
            print("예약한 적이 없습니다.")

    def board(self, clsAir:'class airport_system'):
        if self.name in clsAir.checkinAIR:
            for i in clsAir.checkinAIR[self.name]:
                
                location = clsAir.checkinDATE[self.name][clsAir.checkinAIR[self.name].index(i)]
                answer = input(f"\n\n {i} 항공사, {location} 날짜에 예약된 비행기 타시겠습니까? (y/n) ")

                if answer == 'y':
                    print("탑승 중...")
                    time.sleep(2)
                    clsAir.checkinAIR[self.name].remove(i)
                    clsAir.checkinDATE[self.name].remove(location)

                    print("\n\n-------system-------\n\n탑승 완료되었습니다!\n\n--------------\n")
        else :
            print("탈 항목이 없습니다.")
            
        

class airport_system():
    def __init__(self):
        self.airScheduleAIR = {}
        self.airScheduleDATE = {}
        self.checkinAIR = {}
        self.checkinDATE = {}


    def checkIn(self, airN :'airlines name',date : 'date what you want to checkin', clsPass:'passenger class'):
        if clsPass.name in (self.airScheduleAIR and self.airScheduleDATE):
            
            names = clsPass.name
            if airN in self.airScheduleAIR[names] and date in self.airScheduleDATE[names]:
                
                agree = input("체크인 하시겠습니까? (y/n) ")
                if agree == 'y':
                    
                    if names not in self.checkinAIR:
                        self.checkinAIR[names] = list()
                        self.checkinDATE[names] = list()
                    print("---잠시만 기다려 주세요...---")
                    time.sleep(3.0)
                    
                    print("-------system-------\n\n체크인이 완료되었습니다!\n")
                    self.checkinAIR[names].append(airN)
                    self.checkinDATE[names].append(date)
                    print("--------------")
                
                else :
                    print("\n------- 취소되었습니다. -------\n\n")
                
            else :
                print("체크인 할 날짜나 항공사가 없습니다.")

        else :
            print("예약한 적이 없습니다.")


class airline():
    def __init__(self):
        self.airlines = ['sun_air', 'korea_air', 'mountain_air', 'cloud_air', '1st_air', 'foru_air']
        self.all_Schedule = {
                            'sun_air': ['1/12', '1/14', '1/19', '1/21', '2/1', '2/15'],
                            'korea_air': ['1/30', '2/14', '2/15', '2/16'],
                            'moutain_air': ['1/30', '2/21','3/21'],  
                            'cloud_air': ['1/12', '1/15', '1/16', '1/21', '2/9', '2/10', '3/1', '3/12'],
                            '1st_air': ['1/21', '1/23', '2/1', '2/3', '2/5', '2/7', '2/9'],
                            'foru_air': ['1/22', '1/23', '2/5', '2/7', '2/9', '2/14', '2/21']
                            }

    def del_airline(self, dele):
        try :
            del self.airlines[self.airlines.index(dele)]
            del self.al_Schedule[dele]
        
        except ValueError:
            print(f"That airline : \'{dele}\' does not exist.")

    def create_airlines(self, name : ''):
        
        if name not in self.airlines:
            self.airlines.append(name)
            self.al_Schedule[name] = []
            print("항공사가 추가되었습니다.")

        else :
            print("이미 다른 항공사가 있습니다.")

    def create_schedule(self, airline : 'integer',schedule : 'string'):
        
        if airline in self.airlines :
            self.al_Schedule[airline].appned(schedule)

        else :
            print(f"{airline} 항공사는 존재하지 않습니다.")


def release():
    version = '1.0.2'

    print(f">>> [ Airport System Implementation Program ] release tag : {version} // Made by Cloudy // MIT LICENSE\n")


if __name__ == "__main__":
    release()
    
    airline = airline()
    airport = airport_system()

    a = passenger('hoho')
    a.reservation('korea air', '2/14',airline, airport)

    print(airport.airScheduleAIR)
    print(airport.airScheduleDATE)

    a.cancel_reservation('korea air','2/14',airport)

    print(airport.airScheduleAIR)
    print(airport.airScheduleDATE)

    airport.checkIn('korea air','2/14',a)

    print(airport.checkinAIR)
    print(airport.checkinDATE)

    a.board(airport)

    


