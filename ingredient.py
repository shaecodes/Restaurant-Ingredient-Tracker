from datetime import date
import datetime as dt

class Ingredient:
    def __init__(self, name, stock_quantity, threshold) -> None:
        self.name = name
        self.stock_quantity = int(stock_quantity)  # Convert to integer
        self.threshold = int(threshold)  # Convert to integer

    def restock(self, amount):
        self.stock_quantity += int(amount)
        self._update_stock_file()
        print(f"Restocked {amount} units of {self.name}. Current amount is: {self.stock_quantity} \n")
        today = date.today() #saves the day in hh/mm/ss
        time = dt.datetime.now().strftime("%H:%M:%S") #saves the time in this format
        log_message = (f"Restocked {amount} units on {today} at {time}")
        log_stock(self, log_message)

    def check(self):
        if self.stock_quantity <= self.threshold:
            print(f"ALERT: Low Stock. Current amount of {self.name} is {self.stock_quantity} \n")
            today = date.today()
            time = dt.datetime.now().strftime("%H:%M:%S")
            log_message = (f"Low Stock Alert for {self.name} on {today} at {time}")
            log_stock(self, log_message)
            return True
        else:
            print(f"Restock not required. Current amount of {self.name} is {self.stock_quantity} \n")
            return False

    def use(self, amount):
        if self.check() != True:
            if self.stock_quantity >= int(amount):
                self.stock_quantity -= int(amount)
                print(f"Used {amount} of {self.name}. Current amount is {self.stock_quantity} \n")
                self._update_stock_file()
                today = date.today()
                time = dt.datetime.now().strftime("%H:%M:%S")
                log_message = (f"Used {amount} units on {today} at {time}")
                log_stock(self, log_message)
            else:
                print("Amount needed is more than available. Please restock")
        if self.check() == True:
            print(f"ALERT: Low Stock. Current amount of {self.name} is {self.stock_quantity} \n")
    
    def _update_stock_file(self):
        try:
            with open('ingredients.txt', 'r+') as f:
                lines = f.readlines()  # read all lines from the file
                updated_lines = []  # list to store updated lines
                updated = False  # flag to track if the ingredient has been updated
                for line in lines:
                    if self.name in line:
                        line = line.split(',')
                        line[1] = str(self.stock_quantity)
                        line = ','.join(line)
                        updated = True  # set the flag to True as ingredient has been updated
                    updated_lines.append(line)  # add line to updated lines list
                f.seek(0)  # move file pointer to the beginning
                f.truncate()  # truncate the file to remove old contents
                f.writelines(updated_lines)  # write updated lines back to the file
                if not updated:
                    # if ingredient not found in file, append it to the end
                    f.write(f"{self.name},{self.stock_quantity},{self.threshold}\n")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    
    def add(self, name, stock_quantity, threshold):
        try:
            with open('ingredients.txt', 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if name in line:
                        print("Item already exists")
                        return
                    f.write(line)
                print(f"{stock_quantity} {name} as been added to the inventory")
                f.write(f"{name},{stock_quantity},{threshold}\n")
                today = date.today()
                time = dt.datetime.now().strftime("%H:%M:%S")
                log_message = (f"{name} was added to Inventory on {today} at {time}")
                log_stock(self, log_message)
        except FileNotFoundError as e:
            print(f"Error: {e}")
        

    
    def delete_ingredient(self, name):
        try:
            with open('ingredients.txt', 'r+') as f:
                lines = f.readlines()  
                updated_lines = [] 
                for line in lines:
                    if name in line:  
                        continue  # skip the line if ingredient name is found
                    updated_lines.append(line)  # add line to updated lines list if ingredient name is not found
                f.seek(0)  
                f.truncate()  # truncate the file to remove old contents
                f.writelines(updated_lines)  # write updated lines back to the file
                print(f"Ingredient '{name}' has been deleted from the Inventory.")
                today = date.today()
                time = dt.datetime.now().strftime("%H:%M:%S")
                log_message = (f"Deleted from Inventory on {today} at {time}")
                log_stock(self, log_message)
        except FileNotFoundError  as e:
            print(f"Error: {e}")


def log_stock (self, message):
    with open("log_file.txt", 'a+') as f:
        f.write(f"{self.name}: {message}\n")





