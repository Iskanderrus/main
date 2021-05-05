class RaR:

    def __init__(self, rar_id, name, family_name, partner, location,
                 field_sales, supervisor, net_salary, net_transport_costs,
                 rar_type, status):
        self.id = rar_id
        self.name = name
        self.family_name = family_name
        self.partner = partner
        self.field_sales = field_sales
        self.supervisor = supervisor
        self.location = location
        self.net_salary = net_salary
        self.net_transport_costs = net_transport_costs
        self.rar_type = rar_type
        self.status = status
        self.target_m1q1 = 0
        self.target_m1q2 = 0
        self.target_m1q3 = 0
        self.target_m1q4 = 0
        self.target_m2q1 = 0
        self.target_m2q2 = 0
        self.target_m2q3 = 0
        self.target_m2q4 = 0
        self.target_m3q1 = 0
        self.target_m3q2 = 0
        self.target_m3q3 = 0
        self.target_m3q4 = 0
        self.target_m4q1 = 0
        self.target_m4q2 = 0
        self.target_m4q3 = 0
        self.target_m4q4 = 0
        self.fact_m1q1 = 0
        self.fact_m1q2 = 0
        self.fact_m1q3 = 0
        self.fact_m1q4 = 0
        self.fact_m2q1 = 0
        self.fact_m2q2 = 0
        self.fact_m2q3 = 0
        self.fact_m2q4 = 0
        self.fact_m3q1 = 0
        self.fact_m3q2 = 0
        self.fact_m3q3 = 0
        self.fact_m3q4 = 0
        self.fact_m4q1 = 0
        self.fact_m4q2 = 0
        self.fact_m4q3 = 0
        self.fact_m4q4 = 0
        self.transport_q1 = 0
        self.transport_q2 = 0
        self.transport_q3 = 0
        self.transport_q4 = 0

    def bds_type_change(self, commodity):
        self.rar_type = f"BDS {commodity}"

    def field_type_change(self, location):
        self.rar_type = f"Regional - {location}"

    def kam_type_change(self, ka, location):
        self.rar_type = f"KA - {ka} in {location}"

    def quarterly_salary_calculation(self, rar_id):
        pass

    def salary_increase(self, rar_id, amount):
        pass

    def transport_costs_review(self, rar_id, amount):
        pass

    def rar_efficiency(self, rar_id):
        pass

    def targets_calculation(self, rar_id):
        pass
