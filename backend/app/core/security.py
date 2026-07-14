from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

print("Testing bcrypt...")
print(pwd_context.hash("password123"))