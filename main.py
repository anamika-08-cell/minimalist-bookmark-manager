#fastapi & jinja2 ko aaps mai jodenge...

from fastapi import FastAPI, Request,Depends, Form 
from fastapi.responses import RedirectResponse 
from fastapi.templating import Jinja2Templates
from model import Base, engine, SessionLocal, Bookmark
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

#auto database table create ho jayegi.
Base.metadata.create_all(bind = engine)

#fast api initiate.
app = FastAPI()

# jinja2 templates ko configur krna.
# all html page in templates folder.
templates = Jinja2Templates(directory = "templates")

#Dependency Injection.
def get_db():
    db = SessionLocal()
    try:
          yield db
    finally:
           db.close()

#homepage route.
@app.get("/")
def read_root(request: Request, db: Session = Depends(get_db)):
  msg = None
  try:
      bookmarks = db.query(Bookmark).order_by(Bookmark.id.desc()).all()
      #html file ko render krna ya dikhana.

  except SQLAlchemyError as e:
    print(f"Database Fetch Error: {e}")
    bookmarks = [ ]
    msg = "facing problem to load data from database."

  if not msg:
      msg = "Welcome to Bookmark store & fill your life with happiness!"

  return templates.TemplateResponse(request, name = "index.html"  ,context = {
            "request": request,
            "bookmarks": bookmarks,
            "msg": msg
        })

# form data collection.
@app.post("/add")
def add_bookmark(title:str = Form(...), url : str = Form(...), notes :str = Form(None),db: Session = Depends(get_db)):
    #input validation format check krna.
    title = title.strip()
    url = url.strip()

    if not url.startswith(("http://","https://")):
        url = "https://" + url  #useer url ko valide url banana.

    try:    
        #new bookmark objecct.
        new_bookmarks = Bookmark(title=title, url=url, notes=notes)

        #database mai save karo.
        db.add(new_bookmarks)
        db.commit()
        db.refresh(new_bookmarks)

        return RedirectResponse(url="/", status_code= 303)  

    except SQLAlchemyError as e:
        db.rollback()
        print(f"database insert error: {e}")
        return RedirectResponse(url=" /?msg = Could not save book mark. database error.", status_code=303)

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return RedirectResponse(url="/?msg = Something went wrong please try again.", status_code=303)

@app.post("/delete/{bookmark_id}")
def delete_bookmark(bookmark_id:int, db: Session = Depends(get_db)):

  try:
        #search that id one bookmark.
        bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
        if bookmark:
            db.delete(bookmark)
            db.commit()
        return RedirectResponse(url="/", status_code=303)  
  except SQLAlchemyError as e:
      db.rollback()
      print(f"database delete error: {e}")
      return RedirectResponse (url="/", status_code=303)

  except Exception as e:
      print(f"Unexpected Delete Error :{e}")
      return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0" , port=8000)
      