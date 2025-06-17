from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database.database import Base

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    seller_id = Column(Integer)
    cash_register_id = Column(Integer)
    transaction_time = Column(DateTime)
    transaction_audio = Column(String)

    rating = relationship("Rating", back_populates="transaction", uselist=False)

class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey("transaction.id"), unique=True)
    rating_transaction = Column(Integer)

    transaction = relationship("Transaction", back_populates="rating")