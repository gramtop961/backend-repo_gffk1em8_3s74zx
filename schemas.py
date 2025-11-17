"""
Database Schemas for Dusk Society Media (DSM)

Each Pydantic model represents a MongoDB collection. The collection name is the
lowercased class name.
"""
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List


class Brief(BaseModel):
    """
    Incoming brand/artist brief submissions
    Collection: "brief"
    """
    type: str = Field(..., description="brief type: brand | artist")
    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    handle: Optional[str] = Field(None, description="social handle or website")
    subject: str = Field(..., min_length=2, max_length=200)
    message: str = Field(..., min_length=10, max_length=5000)
    budget_range: Optional[str] = Field(None, description="e.g., <$1k, $1k-$5k, $5k-$20k, >$20k")
    timeline: Optional[str] = Field(None, description="timeline or deadline")
    references: Optional[List[HttpUrl]] = Field(default=None, description="reference links")


class Creator(BaseModel):
    """
    Creator recruitment applications
    Collection: "creator"
    """
    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    city: Optional[str] = None
    discipline: str = Field(..., description="e.g., filmmaker, photographer, editor, writer")
    portfolio: Optional[HttpUrl] = Field(None, description="portfolio link")
    instagram: Optional[str] = None
    gear: Optional[str] = Field(None, description="notable gear")
    bio: Optional[str] = Field(None, max_length=1000)


class Subscriber(BaseModel):
    """
    Email subscribers
    Collection: "subscriber"
    """
    email: EmailStr
    source: Optional[str] = Field(None, description="where the signup came from, e.g., hero, footer")


class Work(BaseModel):
    """
    Showcase items (optional use)
    Collection: "work"
    """
    title: str
    image: HttpUrl
    tags: Optional[List[str]] = None
    url: Optional[HttpUrl] = None
