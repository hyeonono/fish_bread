class BreadShop:
    def __init__(self):
        self.stock={"팥": 10,"슈크림": 8,"초코": 5,}
        self.sales={"팥" : 0,"슈크림": 0,"초코" : 0}
        self.price={"팥": 1000,"슈크림": 1200,"초코": 1500}

    def order_bread(self):
        while True:
            bread_type = input("주문할 붕어빵 맛을 선택하십시오(팥,슈크림,초코,처음으로):")
            if bread_type not in ["팥","슈크림","초코","처음으로"]:
                print("다시 입력하시오")
            if bread_type=="처음으로":
                break
            bread_count = int(input(f"주문할 개수를 입력하시오 현재개수({self.stock[bread_type]}개):"))
            if  self.stock[bread_type] >= (bread_count):
                self.stock[bread_type] -= bread_count
                self.sales[bread_type] += bread_count
                print(f"손님께서 주문하신 {bread_type}붕어빵 {bread_count}개 나왔습니다")
            else:
                print("재고가 부족합니다")


        #붕어빵 admin 기능

    def admin_order(self):
        while True:
            bread_type = input(     "관리자모드를 실행하겠습니다 (붕어빵투입, 처음으로):")
            if bread_type !="붕어빵투입":
                print("다시 입력하시오")
            if bread_type=="처음으로":
                break
            bread_type = input(f"투입할 붕어빵 맛을 선택하시오(팥,슈크림,초코,처음으로):")
            if bread_type == "처음으로":
                break
            bread_count = int(input(f"투입할 개수를 입력하시오. 현재개수({self.stock[bread_type]}개):"))
            if bread_count > 0:
                self.stock[bread_type] += bread_count
                print(f"{bread_type}붕어빵 {bread_count}개 넣었습니다")
            else:
                print("다시 입력하십시오")

    def calculate_sales(self):
        total = 0
        for key in self.sales:
            total += int(self.sales[key] * self.price[key])

        print(f"오늘의 총매출은 {total}원입니다")

