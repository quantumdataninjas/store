# from project import db


# class UserEmail(db.Model):
#     __tablename__ = "user_email"
#     user_id = db.Column(
#         db.BigInteger, db.ForeignKey("user.id"), primary_key=True
#     )
#     user = db.relationship(
#         "User", back_populates="user_emails"
#     )
#     email_id = db.Column(
#         db.BigInteger, db.ForeignKey("email.id"), primary_key=True
#     )
#     email = db.relationship(
#         "Email", back_populates="email_users"
#     )

# email_simple_user = db.Table("email_simple_user",
#     db.Base.metadata,
#     db.Column("email", db.Integer, db.ForeignKey("email.id")),
#     db.Column("simple_user", db.Integer, db.ForeignKey("simple_user.id")),
#     db.Column("created_at", db.DateTime, index=True, default=datetime.utcnow)
# )
