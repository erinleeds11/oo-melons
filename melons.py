"""Classes for melon orders."""

class AbstractMelonOrder():
    
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.tax = tax
        self.order_type = order_type
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species = "christmas":
            base_price *= 1.5

        if self.order_type == "international" and self.qty <10:

            total = (1 + self.tax) * self.qty * base_price + 3
        else:

            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", .08)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", .17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty, passed_inspection):
        super().__init__(species, qty, "government", 0)
        self.passed_inspection = False

    def mark_inspection(passed):
        if passed:
            self.passed_inspection = True



