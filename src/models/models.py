from sqlalchemy import (
    BLOB,
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship

from ..dao.db import Base


class UserChatAssociation(Base):
    __tablename__ = "user_chat_association"
    user_id = Column(Integer, ForeignKey("user_data.id"), primary_key=True)
    chat_id = Column(Integer, ForeignKey("chat_data.id"), primary_key=True)
    waifu_id = Column(Integer, ForeignKey("user_data.id"), default=None)
    is_bot_admin = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class UserData(Base):
    __tablename__ = "user_data"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    full_name = Column(String, nullable=False)
    avatar_small_blob = Column(BLOB, default=None)
    avatar_big_blob = Column(BLOB, default=None)
    avatar_big_id = Column(String, default=None)

    chats = relationship(
        "ChatData",
        secondary=UserChatAssociation.__tablename__,
        back_populates="members",
        primaryjoin="UserData.id==UserChatAssociation.user_id",
        secondaryjoin="ChatData.id==UserChatAssociation.chat_id",
    )

    quotes = relationship("Quote", back_populates="user")

    is_married = Column(Boolean, default=False)
    married_waifu_id = Column(Integer, default=None)
    waifu_mention = Column(Boolean, default=True)

    is_bot = Column(Boolean, default=False)
    is_real_user = Column(Boolean, default=True)  # 频道身份, bot, 匿名用户等 为 False
    is_bot_global_admin = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint(
            "is_married = 0 OR (is_married = 1 AND married_waifu_id IS NOT NULL)"
        ),
    )


class ChatData(Base):
    __tablename__ = "chat_data"
    id = Column(Integer, primary_key=True, index=True)
    quote_probability = Column(Float, default=0.001)
    title = Column(String, nullable=False)
    members = relationship(
        "UserData",
        secondary=UserChatAssociation.__tablename__,
        back_populates="chats",
        primaryjoin="ChatData.id==UserChatAssociation.chat_id",
        secondaryjoin="UserData.id==UserChatAssociation.user_id",
    )
    greet = Column(String, default=None)

    quotes = relationship("Quote", back_populates="chat")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Quote(Base):
    __tablename__ = "quotes"
    chat_id = Column(Integer, ForeignKey("chat_data.id"))
    message_id = Column(Integer, nullable=False)
    link = Column(String, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_data.id"))
    qer_id = Column(Integer)  # 使用 q 的人
    text = Column(String, nullable=True, default=None)
    img = Column(String, nullable=True, default=None, comment="图片的 file id")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("UserData", back_populates="quotes")
    chat = relationship("ChatData", back_populates="quotes")
