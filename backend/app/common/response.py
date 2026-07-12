from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from typing import Any

class SuccessResponse(JSONResponse):
    def __init__(self,
                 status_code: int = status.HTTP_200_OK,
                 code: int = 200,
                 message: str = None,
                 data: Any = None):
        self.code = code
        self.message = message
        self.data = data
        context = {"code": self.code, "message": self.message, "data": self.data}
        super().__init__(content=jsonable_encoder(context), status_code=status_code)
        self.headers["Content-Type"] = "application/json; charset=utf-8"