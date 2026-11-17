def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.
    """
    bmi = weight / (height ** 2)
    return bmi


def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    print("Your BMI is: {:.2f}".format(bmi))


if __name__ == "__main__":
    main()
