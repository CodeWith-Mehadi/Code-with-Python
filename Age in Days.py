age_in_days = int(input())

years = age_in_days // 365
rd = age_in_days % 365

months = rd // 30
days = rd % 30

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")

