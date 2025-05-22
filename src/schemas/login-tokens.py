from pydantic import BaseModel

import datetime


class GetLoginToken(BaseModel):
    id: int
    user_id: int
    token: str
    created_at: datetime
    expires_at: datetime
    revoked: bool
