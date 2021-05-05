class RaR:

    def __init__(self, name, family_name, partner, location,
                 field_sales, supervisor, net_salary, net_transport_costs,
                 type, status):
        self.name = name
        self.family_name = family_name
        self.partner = partner
        self.field_sales = field_sales
        self.supervisor = supervisor
        self.location = location
        self.net_salary = net_salary
        self.net_transport_costs = net_transport_costs
        self.type = type
        self.status = status

    def bds_type_change(self, commodity):
        self.type = f"BDS {commodity}"

    def field_type_change(self, location):
        self.type = f"Regional - {location}"


rar_1 = RaR("Ivan", "Demidov", "Partner1", "Rostov-on-Don", "Petr Zhmykha", "Atanas Zubka", 40000, 5000, "field",
            "active")
rar_1.bds_type_change("Welding")
rar_1.field_type_change("Voronezh Oblast")

print(rar_1.type)
