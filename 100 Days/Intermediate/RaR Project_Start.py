class RaR:

    def __init__(self, name, family_name, partner, location,
                 field_sales_rep, supervisor, net_salary, net_transport_costs,
                 rar_type, status, phone, email):
        self.phone = phone
        self.email = email
        self.id = 0
        self.name = name
        self.family_name = family_name
        self.partner = partner
        self.field_sales = field_sales_rep
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
        self.probation_start_dd_mm_yyyy = 0
        self.probation_end_dd_mm_yyyy = 0
        self.probation_duration_days = \
            self.probation_end_dd_mm_yyyy - \
            self.probation_end_dd_mm_yyyy
        self.inactive_since_dd_mm_yyyy = 0

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


class RaRPartnerContact:

    def __init__(self, name, family_name, partner, phone, email, birth_date):
        self.name = name
        self.family_name = family_name
        self.partner = partner
        self.phone = phone
        self.email = email
        self.birth_date = birth_date
"""
ID Structure:
First digit: 
    1 - Regional RaR
    2 - KA RaR
    3 - BDS RaR
Second place: 
    Country code, e.g. RU / KZ
Third digit: 
    Region code
Fourth place: 
    Partner code: 
    TA, VS, TR, KL, LO, PK
Fifth place: 
    own unique 4 digits number starting at 0001 
    
Example: 
1RU61TA0001 - TA Field RaR in Russia in Rostov-on-Don with own 
number 0001

NB: If RaR type has to be updated - kind promotion of field RaR to 
KA or BDS RaR, only first part of ID has to be changed - own number
remains immutable.
"""


def rar_id_generator(rar, list_of_ids):
    pass

