from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import Session, select
from datetime import datetime, timedelta
from database import engine
from models import User

SECRET_KEY = "youre-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Giải thích:
# - `SECRET_KEY`: Khóa bí mật dùng để mã hóa JWT.
# - `ALGORITHM`: Thuật toán mã hóa sử dụng cho JWT
# - `ACCESS_TOKEN_EXPIRE_MINUTES`: Thời gian hết hạn của token (30 phút).
# - `oauth2_scheme`: Cấu hình OAuth2 để lấy token từ yêu cầu.
# - OAuth2PasswordBearer: Là một lớp bảo mật FastAPI để xử lý xác thực người dùng thông qua token.
# - `pwd_context`: Cấu hình để mã hóa mật khẩu người dùng.
# - CryptContext: Là một lớp từ Passlib để mã hóa và xác thực mật khẩu.

# Hàm xử lý mật khẩu:
def verify_password(plain_password, hased_password):
    return pwd_context.verify(plain_password, hased_password)

def get_password_hash(password):
    return pwd_context.hash(password)

# Giải thích:
# - `verify_password`: Hàm để xác thực mật khẩu người dùng so với mật khẩu đã mã hóa. 
# - `get_passwword_hash`: Hàm để mã hóa mật khẩu người dùng trước khi lưu vào cơ sở dữ liệu.

# Hàm xác thực và tạo JWT:
def authenticate_user(username: str, password: str):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Giải thích:
# - `authenticate_user`: Hàm để xác thực người dùng bằng cách kiểm tra tên người dùng và mật khẩu
# - `create_access_token`: Hàm để tạo JWT với dữ liệu người dùng và thời gian hết hạn.
# - to_encode: Tạo một bản sao của dữ liệu để thêm thời gian hết hạn.
# - `expire`: Tính toán thời gian hết hạn của token bằng cách cộng thời gian hiện tại với khoảng thời gian hết hạn.
# - `jwt.encode`: Mã hóa dữ liệu thành JWT bằng khóa bí mật và thuật toán đã chỉ định.

# Đọc token và lấy user từ token:
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Coild not validate credentaials",
        headers={"WW-Authenticate": "Bearer"},
    )
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if user is None:
            raise credentials_exception
        return user
    
# Giải thích:
# - `get_current_user`: Hàm để lấy người dùng hiện tại từ token.
# - `Depends(oauth2_scheme)`: Sử dụng OAuth2 để lấy token từ request
# - `credentials_exception`: Tạo một ngoại lệ HTTP nếu không thể xác thực token.
# - `jwt.decode`: Giải mã token để lấy payload chứa thông tin người dùng.
# - `payload.get("sub")`: Lấy tên người dùng từ payload.
# - `Session(engine)`: Mở một phiên làm việc với cơ sở dữ liệu để truy vấn người dùng.
