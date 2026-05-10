from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    facebook_id = Column(String, unique=True)
    name = Column(String, nullable=True)

    phone = Column(String, nullable=True)
    location = Column(String, nullable=True)

    project_type = Column(String, nullable=True)

    budget = Column(String, nullable=True)

    lead_status = Column(String, default="NEW")

    created_at = Column(DateTime, default=datetime.utcnow)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    facebook_id = Column(String)

    role = Column(String)

    content = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)