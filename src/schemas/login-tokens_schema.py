from pydantic import BaseModel

import datetime

class Token(BaseModel):
    ...


class GetLoginToken(Token):
    id: int
    user_id: int
    token: str
    revoked: bool
    created_at: datetime
    expires: datetime
