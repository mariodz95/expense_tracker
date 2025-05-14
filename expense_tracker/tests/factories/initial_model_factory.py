from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import scoped_session, sessionmaker

from tests.conftest import engine

session = scoped_session(
    sessionmaker(class_=AsyncSession, bind=engine, autoflush=False)
)


class InitialBaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = session

    created_by = "test"

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = kwargs.pop("session", cls._meta.sqlalchemy_session)

        async def create_async():
            obj = model_class(*args, **kwargs)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

        return create_async()
