class Business:
    def __init__(self, company_name, owner_name, phone_number, additional_phone_number, email, location):
        self.company_name = company_name
        self.owner_name = owner_name
        self.phone_number = phone_number
        self.additional_phone_number = additional_phone_number
        self.email = email
        self.location = location
        self.services = []  

    def add_service(self, service):
        self.services.append(service)

    def __str__(self):
        services_str = "\n".join(f" - {service}" for service in self.services)
        return f"Business: {self.company_name}\nOwner: {self.owner_name}\nPhone: {self.phone_number}\n" \
               f"Additional Phone: {self.additional_phone_number}\nEmail: {self.email}\nLocation: {self.location}\n" \
               f"Services:\n{services_str}"