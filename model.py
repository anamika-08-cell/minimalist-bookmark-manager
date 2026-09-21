#database setup !!
from datetime import datetime, timezone #bookmark kis time pe save hua hai.
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#database ki file ka rasta.(local SQL file)
DATABASE_URL = "sqlite:///./bookmarks.db"

#engine of database.
engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread": False
})

#database ka connection sambhalne ke liye.
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

#base class jisse hamara model banega.
Base = declarative_base()

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key = True)
    title = Column(String(200), nullable=False)
    url = Column(String(500), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
                                         #automatic time stamp hai.
                                         
#debugging ke liye hai.
    def __repr__(self):
        return f'<Bookmark {self.title}>'