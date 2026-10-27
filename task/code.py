students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    sid = input("Student ID: ")
    name = input("Name: ")

    aggregate = float(input("Aggregate Marks: "))

    sub1 = int(input("Subject 1 Marks: "))
    sub2 = int(input("Subject 2 Marks: "))
    sub3 = int(input("Subject 3 Marks: "))

    attendance = float(input("Attendance (%): "))
    income = int(input("Family Income: "))

    subjects = [sub1, sub2, sub3]

    if (aggregate >= 75 and
            min(subjects) >= 60 and
            attendance >= 85 and
            income <= 300000):

        students.append({
            "id": sid,
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income,
            "core": sub1
        })

students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        -x["core"],
        x["id"]
    )
)

print("\nEligible Students Ranking")
print("-" * 50)

rank = 1
for s in students:
    print(rank, s["id"], s["name"],
          "Aggregate =", s["aggregate"])
    rank += 1
