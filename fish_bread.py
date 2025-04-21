# 주문,관리자,종료 이 3가지 선택에 통해서 각각 기능이 적용될수있게할수있다.
while True:
    mode = input("원하는 주문을 선택하세요(주문, 관리자, 종료):")
    if mode =="종료":
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_order()
        
print("시스템이 종료되었습니다")
