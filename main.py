from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import data

app = FastAPI(title="SistemaGestor Pro")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ── Page routes ───────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    sprint4_tasks = [t for t in data.tasks if t.sprint == 4]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "current_page": "index",
        "team": data.team,
        "metrics": data.metrics,
        "sprints": data.sprints,
        "tasks": sprint4_tasks,
        "activity": data.activity,
    })


@app.get("/backlog", response_class=HTMLResponse)
async def backlog(request: Request):
    return templates.TemplateResponse("backlog.html", {
        "request": request,
        "current_page": "backlog",
        "tasks": data.tasks,
        "sprints": data.sprints,
        "requirements": data.requirements,
    })


@app.get("/design", response_class=HTMLResponse)
async def design(request: Request):
    return templates.TemplateResponse("design.html", {
        "request": request,
        "current_page": "design",
        "entities": data.entities,
        "sprints": data.sprints,
        "tools": data.tools,
    })


@app.get("/development", response_class=HTMLResponse)
async def development(request: Request):
    return templates.TemplateResponse("development.html", {
        "request": request,
        "current_page": "development",
        "metrics": data.metrics,
    })


@app.get("/testing", response_class=HTMLResponse)
async def testing(request: Request):
    return templates.TemplateResponse("testing.html", {
        "request": request,
        "current_page": "testing",
        "tests": data.tests,
        "bugs": data.bugs,
    })


@app.get("/deployment", response_class=HTMLResponse)
async def deployment(request: Request):
    return templates.TemplateResponse("deployment.html", {
        "request": request,
        "current_page": "deployment",
        "tools": data.tools,
    })


# ── API routes ────────────────────────────────────────────────────────────────

@app.get("/api/team")
async def api_team():
    return [m.model_dump() for m in data.team]

@app.get("/api/requirements")
async def api_requirements():
    return [r.model_dump() for r in data.requirements]

@app.get("/api/sprints")
async def api_sprints():
    return [s.model_dump() for s in data.sprints]

@app.get("/api/tests")
async def api_tests():
    return [t.model_dump() for t in data.tests]

@app.get("/api/bugs")
async def api_bugs():
    return [b.model_dump() for b in data.bugs]

@app.get("/api/metrics")
async def api_metrics():
    return [m.model_dump() for m in data.metrics]

@app.get("/api/tasks")
async def api_tasks(sprint: int | None = None):
    result = data.tasks
    if sprint:
        result = [t for t in result if t.sprint == sprint]
    return [t.model_dump() for t in result]

@app.get("/api/activity")
async def api_activity():
    return [a.model_dump() for a in data.activity]
