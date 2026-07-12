from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, DateTime
from typing import Optional
from app.core.base_model import Base




class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, comment="用户表主键ID")
    username: Mapped[str] = mapped_column(String(64), nullable=False, comment="用户名称")
    password: Mapped[str] = mapped_column(String(255), nullable=False, comment="加密密码")
    name: Mapped[Optional[str]] = mapped_column(String(32), nullable=True,  comment="用户昵称")
    avatar: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, comment="用户头像地址")
    email: Mapped[Optional[str]] = mapped_column(String(64), nullable=True, comment="用户邮箱")
    is_supper: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否为管理员")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment="注册时间")