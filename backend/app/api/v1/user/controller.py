from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.user.model  import User
from app.api.v1.user.schema import UserRegisterSchema, UserOutSchema
from app.core.dependencies import db_getter
from app.api.v1.user.crud import create_user, check_user
from app.utils.hash_util import PwdUtil
from app.common.response import SuccessResponse

UserRouter = APIRouter(prefix="/user", tags=["系统管理", "用户管理"])


@UserRouter.post("/register",
                 summary="注册用户")
async def register(userdata: UserRegisterSchema,
                   db: AsyncSession = Depends(db_getter)):

    # result = await db.execute(select(User).where(User.username == userdata.username))
    user = await check_user(db, userdata)
    if user:
        raise HTTPException(status_code=401, detail="该用户已存在")

    hashed_password = PwdUtil.hash_password(userdata.password)
    userdata.password = hashed_password

    user: User = await create_user(db, userdata)

    # data = {"username": user.username,
    #             "name": user.name,
    #             "avatar": user.avatar,
    #             "email": user.email,
    #             "is_super": user.is_supper}
    data = UserOutSchema.model_validate(user)

    return SuccessResponse(message="注册成功",data=data.model_dump())