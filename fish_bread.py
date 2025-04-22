# 주문,관리자,종료 이 3가지 선택에 통해서 각각 기능이 적용될수있게할수있다.
stock =  { #key값을 이용해서 value 딕셔너리 써야하는 상황은 어떤 스토리 기반으로 데이터가 구성되었을때
    "팥": 10,
    "슈크림": 8,
    "초코": 5,
}

sales = {
    "팥" : 0,
    "슈크림" : 0,
    "초코" : 0,
}
def order_bread():
    while True:
        bread_type = input("주문할 붕어빵 맛을 선택하십시오(팥,슈크림,초코,처음으로):")
        if bread_type not in ["팥","슈크림","초코","처음으로"]:
            print("다시 입력하시오")
            order_bread()
        if bread_type=="처음으로":
            break
        bread_count = int(input(f"주문할 개수를 입력하시오 현재개수({stock[bread_type]}개):"))
        if stock[bread_type] >= int(bread_count):
            stock[bread_type] -= bread_count
            sales[bread_type] += bread_count
            print(f"손님께서 주문하신 {bread_type}붕어빵 {bread_count}개 나왔습니다")
            order_bread()
        else:
            print(f"재고가 부족합니다")
        


def admin_order():
    while True:
        admin_type = input("관리자모드를 실행하겠습니다")
        if admin_type=="처음으로":
            break

while True:
    mode = input("원하는 주문을 선택하세요(주문, 관리자, 종료):")
    if mode =="종료":
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_order()
        
print("시스템이 종료되었습니다")
