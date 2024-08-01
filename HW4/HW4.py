max=int(input("숫자 게임 최대값을 입력해주세요: "))
min=1
print("1부터까지의 숫자를 하나 생각하세요.")
print("준비가 되었다면 Enter를 누르세요.")
input()
count=0


while True:
  
  purpose=(max+min)//2
  count += 1
  print("당신이 생각한 숫자는",purpose,"입니까?")
  answer=(input("제가 맞췄다면 '맞음', 제가 제시한 숫자보다 크다면 '큼' , 작다면 '작음'을 입력해주세요: "))
  
  if answer == "큼":
    min=purpose
  elif answer == "작음":
    max=purpose
  elif answer == "맞음":
    print(count,"번만에 맞췄다")
    break

    