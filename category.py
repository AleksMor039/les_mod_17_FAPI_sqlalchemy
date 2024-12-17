from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship  # взаимосвязь
from app.models import *


# делаем новую таблицу
class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True) # является ли наша категория активной (по умолчанию True)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)  # подкатегория

    products = relationship("Product", back_populates="category")


from sqlalchemy.schema import CreateTable
print(CreateTable(Category.__table__))

