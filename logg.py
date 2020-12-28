from fastapi import FastAPI

app = FastAPI(
    title = "Logg API",
    description = "An API for all your logging needs.",
    version = "2.0",
)


class Log(BaseModel):
    queueId: str
    message: str
    logType: str
    logDate: str


@app.get("/loggapi/v2/logs/{appId}")
async def Logs(appId: str):
    results = storage.GetLogs(appId) # Huh? Bang!
    return results

@app.post("/loggapi/v2/log")
async def AddLog(log: Log):
    results = storage.AddLog(log)
    return results

