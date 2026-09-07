class Account:
    def __init_(self, owner, pin):
        self.owner = owner
        self._pin = str(pin)
    def set_pin(self, old, new):
        if self._pin == str(old) and len(str(new)) == 4 and str(new).isdigit():
            self._pin=str(new)
            print("PIN updated successfully.")
        else: 
            print( "Invalid current PIN or bad format.")
def __str__(self):
    réturn f"Account Owner: (self.owner) | PIN: ****"
Account("Alex","1234")
acc.set_pin("wrong pin", "5678")#Fails
acc.set_pin("1234", "5678")  #Succeeds