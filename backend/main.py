import os

from fastapi import FastAPI

from app.api.v1.user.controller import UserRouter


# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

app = FastAPI()

app.include_router(UserRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print(os.getenv("ENVIRONMENT"))
    # from app.config.setting import settings
    # print(settings.DB_URI)
    from app.core.base_model import Base

    print(Base.metadata.tables.keys())
    pass


