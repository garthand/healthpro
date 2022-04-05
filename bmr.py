#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Calculates body health statistics"""


class User():
    """Class containing fields and methods for app users"""

    def __init__(self, data):
        """Prepares user variables from provided data dictionary"""
        self.weight_units = data["weight_units"]
        self.height_units = data["height_units"]
        self.weight = float(data["weight"])
        self.height = float(data["height"])
        self.age = float(data["age"])
        self.sex = data["sex"]
        self.standardize_weight()
        self.standardize_height()
        self.bmr = self.calculate_bmr()

    def standardize_weight(self):
        """Ensures that all weights are converted to kg
        for further processing"""
        # If units are already kg no conversion needed
        if self.weight_units == "kg":
            return
        # Convert lbs to kg, rounding up as necessary
        if self.weight_units == "lbs":
            self.weight = round(self.weight * 0.453592)
        # Convert stone to kg, rounding up as necessary
        else:
            self.weight = round(self.weight * 6.35029)

    def standardize_height(self):
        """Ensures that all heights are converted to cm
        for further processing"""
        # If units are already cm no conversion needed
        if self.height_units == "cm":
            return
        # Convert in to cm, rounding up as necessary
        self.height = round(self.height * 2.54)

    def calculate_bmr(self):
        """Calculates basal metabolic rate using the
        Mifflin St Jeor equation"""
        weight_factor = 10.0 * self.weight
        height_factor = 6.25 * self.height
        age_factor = 5.0 * self.age
        if self.sex == "Female":
            sex_factor = -161.0
        else:
            sex_factor = 5.0
        bmr = int(weight_factor + height_factor - age_factor + sex_factor)
        return bmr

    def report_bmr(self):
        """Reports basal metabolic rate"""
        print(self.bmr)


if __name__ == "__main__":
    user_data = {
       "weight_units": "lbs",
       "height_units": "in",
       "weight": "140",
       "height": "69",
       "age": "29",
       "sex": "Male"
    }
    user = User(user_data)
    user.report_bmr()
