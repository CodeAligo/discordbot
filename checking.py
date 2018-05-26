a = []

while True:
    b = input("이름을 입력해주십시오 :")
    if b not in a:
        print("등록되지 않은 이름입니다.")
        print("자동 등록중...")
        a.append(b)
        print("등록 완료!")
        continue

    else:
        print("만나서 반갑습니다. "+b+"님!")
        break
    
   
        
    