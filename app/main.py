from fastapi import FastAPI , HTTPException
import httpx

app=FastAPI()

GITHUB_GISTS_URL = "https://api.github.com/users/{username}/gists"

@app.get("/")
def home():
    return {"message": "FastAPI Docker Public Gists API running!"}

@app.get("/{username}")
async def get_user_gists(username: str):
    url =GITHUB_GISTS_URL.format(username=username)

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code== 404:
        raise HTTPException(status_code=404, detail="GitHub user not found")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="GitHub API error")
    
    gists = response.json()

    # formatted = [
    #     {
    #         "id" : gist["id"],
    #         "description": gist["description"],
    #         "url": gist["html_url"]
    #     }
    #     for gist in gists
    # ]

    return {"user" : username, "gists" : gist}