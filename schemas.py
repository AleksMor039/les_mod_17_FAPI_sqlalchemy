from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str # назв.продукта
    description: str # описание
    price: int # цена
    image_url: str # ссылка на изображение
    stock: int # остаток
    category: int # id-категории


class CreateCategory(BaseModel):
    name: str # назв.категории
    parent_id: int # родитель
