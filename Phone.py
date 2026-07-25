class MobilePhone:
    def __init__(self,model,battery):
        self.model=model
        self.battery=battery
    
    def use_phone(self):
        self.battery-=5

phone1=MobilePhone(14,90)

phone1.use_phone()

print(phone1.battery)