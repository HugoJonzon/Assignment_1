import math
# This is a class that provides valuable data for a second-order high-pass or low-pass filter.
# The class can be run by creating an object of the class and specifying "HP" for a high-pass filter or "LP" for a low-pass filter as the first attribute.
# The class provides data such as the resonance point in hertz, the damping factor, and the transfer function.


class Filter2:  # Class for the filter
    # Class for the filter
    def __init__(self, type=None, Lvalue=None, Cvalue=None, Rvalue=0):
        if type == "HP" or type == "LP":
            self.type = type
        else:
            raise ValueError("Wrong input text.")

        if Lvalue > 0 and Cvalue > 0 and Rvalue >= 0:
            self.Lvalue = Lvalue
            self.Cvalue = Cvalue
            self.Rvalue = Rvalue  # Saves all the atributes is a objekt self
        else:
            raise ValueError("All component values must be positive.")

    # This function calculates the resonans point for the filter and then prints it
    def get_resonance_point(self):
        resonansFreq = 1 / (2 * math.pi * math.sqrt(self.Lvalue * self.Cvalue))
        return round(resonansFreq, 4)

    # This function calculates the damping factor for the filter and then prints it
    def get_damping_factor(self):
        dampingFactor = self.Rvalue / 2 * math.sqrt(self.Cvalue / self.Lvalue)
        return round(dampingFactor, 4)

    # This gets the transfer function. The transfer function for high pass and low pass are differet
    def get_transfer(self):
        if self.type == "LP":
            transfer = "1 / (s^2*{} + s*{} + 1)".format(
                self.Lvalue * self.Cvalue, self.Rvalue * self.Cvalue
            )  # Transfer function string
        elif self.type == "HP":
            transfer = "(s^2*{}) / (s^2*{} + s*{} + 1)".format(
                self.Lvalue * self.Cvalue,
                self.Lvalue * self.Cvalue,
                self.Rvalue * self.Cvalue,
            )
        return transfer
