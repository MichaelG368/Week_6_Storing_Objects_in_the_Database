from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customer(Base):
    def __init__(self, first_name, last_name, gender, address):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address
        self.__reward_points = 0
        
    __tablename__ = "Customers"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    address = Column(String)
    __reward_points = Column(Integer)
    
    def __repr__(self):
        return "Name: {0} {1}, Gender: {2}, Address: {3}, Reward Points: {4}".format(self.first_name, self.last_name, self.gender, self.address, self.__reward_points)
    
def main():
    Engine = create_engine("sqlite:///:memory:", echo=False)
    
    Base.metadata.create_all(Engine)
    
    customer_1 = Customer("Mike", "Everson", "Male", "652 Gold Lane, New York, NY, 05278")
    
    session = sessionmaker(bind=Engine)
    Session = session()
    
    Session.add(customer_1)
    
    Session.add_all([
        Customer("Amy", "Everson", "Female", "652 Gold Lane, New York, NY, 05278"),
        Customer("Rick", "Jackson", "Male", "100 Silver Lane, New York, NY, 05279")])
    Session.commit()
    
    for row in Session.query(Customer).all():
        print(row)
    
main()