import uuid

from fastapi import APIRouter, Depends, Header, HTTPException, status
from models.user import CreateUser, GetUser, UpdateUser

router = APIRouter(tags=["users"], prefix="/users")


users: list[GetUser] = [
    GetUser(nombre="Miltron", apellido="Velazquez", email="miltron@hotmail.com"),
]


def validate_api_key(x_api_key: str = Header(...)):
    if x_api_key != "api":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong Api Key"
        )


@router.get("/{id}", response_model=GetUser)
async def get_user(id, _: None = Depends(validate_api_key)):
    for user in users:
        if id == str(user.id):
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.get("", response_model=list[GetUser])
async def get_users(_: None = Depends(validate_api_key)):
    return users


@router.post("", response_model=GetUser, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, _: None = Depends(validate_api_key)):
    new_user = GetUser(**user.model_dump())
    users.append(new_user)
    return new_user


@router.patch("/{id}", response_model=GetUser, status_code=status.HTTP_200_OK)
async def update_user(
    id: uuid.UUID, up_user: UpdateUser, _: None = Depends(validate_api_key)
):
    for i, user in enumerate(users):
        if user.id == id:
            updated = user.model_copy(update=up_user.model_dump(exclude_unset=True))
            users[i] = updated
            return users[i]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    id: uuid.UUID,
    _: None = Depends(validate_api_key),
):
    for i, user in enumerate(users):
        if user.id == id:
            users.pop(i)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
