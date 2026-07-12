from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schema import UserRegisterSchema
from .model import User
from .schema import UserRegisterSchema



async def check_user(db: AsyncSession, userdata: UserRegisterSchema):
    stmt = select(User).where( User.username == userdata.username)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    return user

async def create_user(db: AsyncSession, userdata:UserRegisterSchema):
    user = User(**userdata.model_dump())
    db.add(user)
    await db.flush()
    await db.refresh(user)
    return user