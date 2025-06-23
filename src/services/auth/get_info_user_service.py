from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.auth.get_info_user_repo import GetInfoUserRepo

class GetInfoUserService:

    @staticmethod
    async def get_user_info_service(user_id: int, session: AsyncSession):
        return await GetInfoUserRepo.get_user_info(user_id, session)
