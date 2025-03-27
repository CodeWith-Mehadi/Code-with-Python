N = int(input())

hours = N // 3600
rs = N % 3600
minutes = rs // 60
seconds = rs % 60

print(f"{hours}:{minutes}:{seconds}")