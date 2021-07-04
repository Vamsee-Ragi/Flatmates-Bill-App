class Bill:
    """
    Object that contains data about the bill such as Total amount and time period during which the bill
    was generated.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains the details about the flatmates, number of days they stayed in the house and the
    amount they have to pay for the time period.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


