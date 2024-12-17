from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship  # взаимосвязь
from app.models import *


# делаем новую таблицу
class Product(Base):
    __tablename__ = "products"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)  # описание товара
    price = Column(Integer)
    image_url = Column(String)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))  # ForeignKey - 1 ко многим
                                                                # (конечности и тело/к 1 категории много товаров)
    rating = Column(Float)
    is_active = Column(Boolean, default=True)  # является ли наша категория активной (по умолчанию True)

    # relationship - показ.взаимосвязь (к кому взаимосвязь) и (куда возвращаться с ней)
    category = relationship("Category", back_populates="products")
