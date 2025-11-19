"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import date

# Example schemas (keep for reference)
class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# ---------------- League App Schemas ----------------
class League(BaseModel):
    """League configuration and season info
    Collection name: "league"
    """
    name: str = Field(..., description="League name")
    city: Optional[str] = Field(None, description="City or region")
    season_start: Optional[date] = Field(None, description="Season start date")
    season_end: Optional[date] = Field(None, description="Season end date")
    divisions: List[str] = Field(default_factory=lambda: ["Recreational", "Intermediate", "Advanced"])
    team_size: int = Field(6, ge=1, le=12, description="Players per team")
    is_open: bool = Field(True, description="Whether registration is open")
    description: Optional[str] = Field(None, description="About the league")

class Registration(BaseModel):
    """Player or team registration
    Collection name: "registration"
    """
    full_name: str = Field(..., description="Registrant full name")
    email: EmailStr = Field(..., description="Contact email")
    phone: Optional[str] = Field(None, description="Phone number")
    pronouns: Optional[str] = Field(None, description="Pronouns")
    division: Optional[str] = Field(None, description="Requested division/skill level")
    team_name: Optional[str] = Field(None, description="Team name if registering a team")
    free_agent: bool = Field(False, description="Registering as a free agent")
    notes: Optional[str] = Field(None, description="Additional info or requests")

class Announcement(BaseModel):
    """League announcements/news
    Collection name: "announcement"
    """
    title: str
    message: str
    published: bool = True
