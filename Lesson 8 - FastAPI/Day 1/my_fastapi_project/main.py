from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from models import Note
from database import create_db_and_tables, engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/notes/")
def create_note(note: Note):
    with Session(engine) as session:
        session.add(note)
        session.commit()
        session.refresh(note)
        return note

@app.get("/notes/")
def read_notes():
    with Session(engine) as session:
        notes = session.exec(select(Note)).all()
        return notes

@app.get("/notes/{note_id}")
def read_note(note_id: int):
    with Session(engine) as session:
        note = session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        return note

@app.put("/notes/{note_id}")
def update_note(note_id: int, updated: Note):
    with Session(engine) as session:
        note = session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")

        note.title = updated.title
        note.content = updated.content

        session.add(note)
        session.commit()
        session.refresh(note)
        return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    with Session(engine) as session:
        note = session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        session.delete(note)
        session.commit()
        return {"deleted": True}