"""
COMP.CS.100 3_8_3 program.
Program that calculates and returns a correct dose when the following initial
values are given: patient's weight, the time from receiving the previous dose,
the previous daily ratio.
Creator: Rahele Ahmadian
Student id number: 151200445
"""

def calculate_dose(patient_weight, time_from_prev_dose, prev_daily_ratio):
    """
    calculates and returns a correct dose of Parasetamol

    :param patient_weight: int, the patient's weight(kg)
    :param time_from_prev_dose: int, time has passed from the previous dose (full hours)
    :param prev_daily_ratio: int, the total dose for the last 24 hours (mg)
    :return correct_dose: int, the correct amount of Parasetamol to give to the patient(mg)
    """
    # administered doses of 15 mg per kilogram of weight(mg)
    each_dose = patient_weight * 15
    # The daily dose cannot be over 4000 mg.
    max_dose = 4000 - prev_daily_ratio
    if time_from_prev_dose >= 6:
        if each_dose > max_dose:
            correct_dose = max_dose
        elif each_dose <= max_dose:
            correct_dose = each_dose
    else:
        correct_dose = 0
    return correct_dose


def main():
    patient_weight = int(input("Patient's weight (kg): "))
    time_from_prev_dose = int(input("How much time has passed from the previous dose (full hours): "))
    prev_daily_ratio = int(input("The total dose for the last 24 hours (mg): "))
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(patient_weight, time_from_prev_dose, prev_daily_ratio)}")

if __name__ == "__main__":
    main()
