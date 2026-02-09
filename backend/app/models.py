from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password_hash: str
    is_admin: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    name: str
    is_kids: bool = Field(default=False)
    pin_hash: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    sort_order: int = Field(default=100)

class Playlist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    source_type: str = Field(default="upload")
    source_value: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Channel(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("url", name="uq_channel_url"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    group: str = Field(default="Sem grupo", index=True)
    logo: Optional[str] = None
    url: str = Field(index=True)
    is_active: bool = Field(default=True)
    category_id: Optional[int] = Field(default=None, foreign_key="category.id", index=True)
    playlist_id: Optional[int] = Field(default=None, foreign_key="playlist.id", index=True)

class Favorite(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("profile_id", "channel_id", name="uq_fav_profile_channel"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", index=True)
    channel_id: int = Field(foreign_key="channel.id", index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class WatchProgress(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("profile_id", "channel_id", name="uq_progress_profile_channel"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", index=True)
    channel_id: int = Field(foreign_key="channel.id", index=True)
    seconds: float = Field(default=0)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# Device approval gate
class DeviceRegistration(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("device_id", name="uq_device_id"),
        UniqueConstraint("virtual_mac", name="uq_virtual_mac"),
    )
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: str = Field(index=True)
    virtual_mac: str = Field(index=True)
    status: str = Field(default="pending", index=True)  # pending|approved|blocked
    device_model: Optional[str] = None
    device_brand: Optional[str] = None
    android_version: Optional[str] = None
    app_version: Optional[str] = None
    first_seen_at: datetime = Field(default_factory=datetime.utcnow)
    last_seen_at: datetime = Field(default_factory=datetime.utcnow)
    approved_by_user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    approved_at: Optional[datetime] = None
    notes: Optional[str] = None

# IPTV sources (M3U URL, Xtream, XMLTV)
class Source(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("name", name="uq_source_name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    type: str = Field(index=True)  # m3u | xtream | xmltv
    url: Optional[str] = None
    resolved_url: Optional[str] = None
    host: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: bool = Field(default=True)
    last_sync_at: Optional[datetime] = None
    last_sync_status: Optional[str] = None
    last_sync_message: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ChannelExt(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("channel_id", name="uq_channelext_channel"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    channel_id: int = Field(foreign_key="channel.id", index=True)
    tvg_id: Optional[str] = Field(default=None, index=True)
    tvg_name: Optional[str] = None
    stream_type: str = Field(default="unknown", index=True)  # hls|mpegts|mp4|unknown
    source_id: Optional[int] = Field(default=None, foreign_key="source.id", index=True)
    xtream_stream_id: Optional[int] = Field(default=None, index=True)
    xtream_category_id: Optional[int] = Field(default=None, index=True)
    is_adult: bool = Field(default=False, index=True)
    min_age: int = Field(default=0, index=True)

class EpgChannelMap(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("channel_id", name="uq_epgmap_channel"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    channel_id: int = Field(foreign_key="channel.id", index=True)
    xmltv_channel_id: str = Field(index=True)
    display_name: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class EpgProgram(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    xmltv_channel_id: str = Field(index=True)
    title: str
    start_utc: datetime = Field(index=True)
    end_utc: datetime = Field(index=True)
    desc: Optional[str] = None
    category: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SourceSyncLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source_id: int = Field(foreign_key="source.id", index=True)
    started_at: datetime = Field(default_factory=datetime.utcnow)
    finished_at: Optional[datetime] = None
    status: str = Field(default="running")  # running|ok|error
    message: Optional[str] = None
