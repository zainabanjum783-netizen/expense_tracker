# class-methods takes input on a loop while keeping a base condition to stop  and use __init__ and then print all data when stop
# Food
# Transport
# Rent / Housing
# Education
# Miscellaneous

class tracker:
    def __init__(self):
        self.storage = {
            'food': 0,
            'transport': 0,
            'housing': 0,
            'education': 0,
            'shopping': 0,
            'miscellaneous': 0
        }
        self.expenses = []
        self.salary = float(input("Enter your salary: "))
        
    def input_store(self):
        while True:
            print('enter 0 to stop and get your summary and insights or 1 to continue entry')
            cond=int(input())
            
            if cond==0:
                self.insights()
                self.summary()
                return
            print('enter name of your expense: ')
            name=input()
            
            print('enter your category of expense: ')
            print(self.storage.keys())
            category=input()
            if category not in self.storage.keys():
                print('invalid input')
                self.insights()
                self.summary()
                break
            print('enter your amount: ')
            price=float(input())
            if price<1:
                print('invalid input')
                tracker.insights()
                tracker.summary()
                break
            self.expenses.extend([name,category,price])
            self.storage[category]+=price
            
    def insights(self):
        maxcat=max(self.storage,key=self.storage.get)
        maxpp=self.storage[maxcat]
        
        mincat=min(self.storage,key=self.storage.get)
        minpp=self.storage[mincat]
        
        print(F'MAXIMUM EXPENSE IS IN THIS CATEGORY: {maxcat.upper()} AND EXPENSE IS: {maxpp}')
        print(F'MINIMUM EXPENSE IS IN THIS CATEGORY: {mincat.upper()} AND EXPENSE IS: {minpp}')

    def summary(self):
        print('EXPENSES CATEGORIES WISE ARE: ')
        print(self.storage)
        
        print('TOTAL EXPENSE: ')
        print(sum(self.storage.values()))
        
        print('PERCENTAGE WISE EXPENSES IN EACH CATEGORY: ')
        for c in self.storage.keys():
            print(c,end=' ')
            print((self.storage[c]/self.salary)*100,'%')
                
a=tracker()
a.input_store()
