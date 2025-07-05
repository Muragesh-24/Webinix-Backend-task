from sqlalchemy import Column, Integer, String
from scripts.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_Completed = Column(Integer, default=0)
