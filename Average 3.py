N1, N2, N3, N4 = map(float, input().split())

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    exam_score = float(input())
    print(f"Nota do exame: {exam_score:.1f}")

    final_average = (media + exam_score) / 2

    if final_average >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {final_average:.1f}")
