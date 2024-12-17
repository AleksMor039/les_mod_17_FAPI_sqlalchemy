from fastapi import APIRouter  # сущность для построения роутинга

router = APIRouter(prefix="/category", tags=["category"])  # сущность позволит раб. с роутингом по префиксу


# конектим декоратор к роутеру
@router.get("/all_categories")
async def get_all_categories():
    pass


@router.post("/create")
async def creaty_category():
    pass


@router.put("/update_category")
async def update_category():
    pass


@router.delete("/delete")
async def delete_category():
    pass
