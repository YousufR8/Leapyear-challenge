print("Leap year.")
year = 2400 and 1989
if year % 4 == 0 and year % 100 > 0:

      print(f"Because {year} is cleanly divisible by 4")

      print(f"And {year} is not cleanly divisible by 100")

elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:

      print(f"Because {year} is cleanly divisible by 4")

      print(f"And {year} is cleanly divisible by 100")

      print(f"And {year} is cleanly divisible by 400")

else:

    print("Normal year.")

    print(f"Because {year} is NOT divisible by 4")