from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Creating an Index on 'name' column
    __table_args__ = (Index('ix_department_name', 'name'),)

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    department = relationship("Department", back_populates="employees")

    # Creating a Foreign Key on 'department_id' referencing 'departments.id'
    __table_args__ = (ForeignKeyConstraint(['department_id'], ['departments.id']),)

Department.employees = relationship("Employee", order_by=Employee.id, back_populates="department")