start = int(input('숫자게임 최대값을 입력해주세요:'))
print('1부터', start, '까지의 숫자를 하나 생각하세요.')
print('준비가 되었으면 Enter를 누르세요.')
input()

min_value = 0
max_value = start
value = int((min_value + max_value)/2)

print('당신이 생각한 숫자는 ',value, '입니까?')
user = input()
count = 1

while user != '맞음':
  if user == '큼':
    min_value = value
    value = int((min_value + max_value)/2)
    print('당신이 생각한 숫자는 ',value, '입니까?')
    count += 1
    user = input()
  elif user == '작음':
    max_value = value
    value = int((min_value + max_value)/2)
    print('당신이 생각한 숫자는 ',value, '입니까?')
    count += 1
    user = input()
if user == '맞음':
  print(count,'번만에 맞췄다.')