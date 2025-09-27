from sqlalchemy import Column, Integer, String
from config.database import Base

class Art(Base):
    __tablename__ = "arts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String)
    year = Column(Integer)
    style = Column(String, nullable=True)
    description = Column(String, nullable=True)
