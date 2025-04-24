from fish_bread_model import BreadShop

shop = BreadShop()

while True:
    print("------------------------------------------")
    mode = input("원하는 주문을 선택하세요(주문, 관리자, 종료):")
    if mode =="종료":
        shop.calculate_sales()
        print("프로그램을 종료합니다")
        break
    elif mode == "주문":
        shop.order_bread()
    elif mode == "관리자":
        shop.admin_order()
        
    print("시스템이 종료되었습니다")

# 로직이 숨겨지고 /유지보수하기 용이함