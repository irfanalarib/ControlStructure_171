percentage = float(input("Masukan persentase nilai siswa"))

if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good Performance")
elif percentage >= 70:
    print("Good Performance")
elif percentage >= 60:
    print("Average Performance")
else:
    print("Needs Improvement")