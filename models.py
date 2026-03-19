from pydantic import BaseModel
from typing import Literal


class TeamMember(BaseModel):
    name: str
    role: str
    technology: str
    email: str


class Requirement(BaseModel):
    id: int
    description: str
    type: Literal["functional", "non-functional"]
    priority: Literal["alta", "media", "baja"]
    validated: bool


class Entity(BaseModel):
    name: str
    fields: list[str]


class Sprint(BaseModel):
    number: int
    name: str
    status: Literal["completado", "en progreso", "pendiente"]
    start_date: str
    end_date: str


class TestResult(BaseModel):
    type: str
    total: int
    passed: int
    description: str


class Bug(BaseModel):
    id: int
    description: str
    severity: Literal["alta", "media", "baja"]
    status: Literal["resuelto", "abierto"]
    resolved_by: str


class Metric(BaseModel):
    label: str
    value: str
    icon: str


class Task(BaseModel):
    id: str
    title: str
    type: Literal["feature", "bug", "chore", "design"]
    status: Literal["todo", "in_progress", "review", "done"]
    priority: Literal["alta", "media", "baja"]
    assignee: str
    assignee_initials: str
    points: int
    sprint: int


class Activity(BaseModel):
    user: str
    initials: str
    action: str
    target: str
    time: str
    type: Literal["commit", "close", "open", "deploy", "approve", "merge", "comment"]
