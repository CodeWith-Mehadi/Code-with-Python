start_day = int(input().split()[1])
h1, m1, s1 = map(int, input().split(" : "))

end_day = int(input().split()[1])
h2, m2, s2 = map(int, input().split(" : "))

start_seconds = (start_day * 86400) + (h1 * 3600) + (m1 * 60) + s1
end_seconds = (end_day * 86400) + (h2 * 3600) + (m2 * 60) + s2

total_seconds = end_seconds - start_seconds

days = total_seconds // 86400
total_seconds %= 86400
hours = total_seconds // 3600
total_seconds %= 3600
minutes = total_seconds // 60
seconds = total_seconds % 60

print(days, "dia(s)")
print(hours, "hora(s)")
print(minutes, "minuto(s)")
print(seconds, "segundo(s)")
