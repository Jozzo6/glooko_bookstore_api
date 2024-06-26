import uuid
from app.database import Base
from sqlalchemy import Column, Text, DateTime, func, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Text, primary_key=True, default=lambda: str(uuid.uuid4()))
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())
    email = Column(Text, unique=True, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    type = Column(Integer, nullable=False, default=1)
    password_hash = Column(Text, nullable=False)

    users_books = relationship('BooksUsers', back_populates='user')

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, first_name={self.first_name}, last_name={self.last_name}, type={self.type})"