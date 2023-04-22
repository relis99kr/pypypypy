PM = float(input("미세면지량 >> "))

if 151 <= PM:
    warn = '매우 나쁨'

elif 81 <= PM:
    warn = "나쁨"

elif 31 <= PM:
    warn = "보통"

else:
    warn = "좋음"

print(f'미세먼지 농도: {PM:.2f}, 등급 {warn}')