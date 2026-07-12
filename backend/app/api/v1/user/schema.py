from datetime import datetime

from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional

class UserRegisterSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=32 ,description="账号")
    password: str = Field(..., min_length=6, max_length=128 ,description="密码")
    name: Optional[str] = Field(default=None, max_length=32, description="昵称")
    # email: Optional[EmailStr,None] = Field(default=None, description="邮箱")
    # avatar: Optional[str, None] = Field(default=None, description="头像地址")

    # @field_validator("username")
    # def validate_username(self,value: str):
    #     v = value.strip()
    #     if not v:
    #         raise ValueError("账号不能为空")
    #
    #     import re
    #     if not re.match(r"^[a-zA-Z][a-zA-Z0-9._-]{2,31}$",v):
    #         raise ValueError("账号需要以字母开头，3-32位，仅允许字母、数字、-._")
    #     return v

class UserOutSchema(BaseModel):
    id: int = Field(..., description="用户ID")
    username: str = Field(..., description="账号")
    name: Optional[str]  = Field(default=None, description="昵称")
    avatar: Optional[str]  = Field(default=None, description="头像地址")
    email: Optional[str] = Field(default=None, description="邮箱")
    is_super: Optional[bool] = Field(default=False, description="是否为管理员")
    created_at: Optional[datetime] = Field(default=None, description="创建时间")

    model_config = ConfigDict(
        from_attributes=True
    )