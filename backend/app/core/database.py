from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


from app.config.setting import settings


def create_async_engine_and_session(db_url:str = settings.ASYNC_DB_URI) :
    try:
        async_engine = create_async_engine(url=db_url,echo=settings.DATABASE_ECHO)
    except Exception as e:
        print(f"数据库连接失败：{e}")
        raise
    else:
        AsyncSessionLocal = async_sessionmaker[AsyncSession](bind=async_engine,expire_on_commit=settings.EXPIRE_ON_COMMIT)
    
        return async_engine, AsyncSessionLocal

async_engine, async_db_session = create_async_engine_and_session()