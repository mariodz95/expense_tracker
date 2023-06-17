from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import scoped_session, sessionmaker

from tests.conftest import engine

session = scoped_session(sessionmaker(class_=AsyncSession, bind=engine, autoflush=True))


class InitialBaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = session

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        async def create_async():
            async with session.begin():
                session.add(model_class(*args, **kwargs))
                await session.commit()
            return model_class(*args, **kwargs)

        return create_async()
