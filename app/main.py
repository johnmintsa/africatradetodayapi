from fastapi import FastAPI
from .router import post,users, auth, vote
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse








#models.Base.metadata.create_all(bind=database.engine)



app = FastAPI()
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AfricanTradeToday - Coming Soon</title>
    <style>
        body {
            background-color: #f7f7f7;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
            padding-top: 100px;
        }
        h1 {
            font-size: 48px;
            color: #0f4d92;
            margin-bottom: 20px;
        }
        p {
            font-size: 24px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>AfricanTradeToday</h1>
        <p>Coming Soon</p>
    </div>
</body>
</html>

"""
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def root():
    return HTMLResponse(html)





app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)