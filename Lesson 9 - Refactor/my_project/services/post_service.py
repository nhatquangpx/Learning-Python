from my_project.models import Post
from my_project.database import engine
from sqlmodel import Session, select
from datetime import datetime

def create_post(post_data, user):
    post = Post(
                title=post_data.title,
                content=post_data.content,
                author_id=user.id,
                created_at=utcnow()
    )
    with Session(engine) as session:
        session.add(post)
        session.commit()
        session.refresh(post)
        return post

def get_all_posts():
    with Session(engine) as session:
        return session.exec(select(Post)).all()
    
def get_user_posts(user):
    with Session(engine) as session:
        return session.exec(
            select(Post).where(Post.author_id == user.id) 
        ).all()