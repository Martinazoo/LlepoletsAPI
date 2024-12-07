from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import meta, engine


users = Table("users", meta, 
              Column("id", Integer, primary_key=True),
              Column("name", String(100)),
              Column("username", String(100), unique=True),
              Column("email", String(100), unique=True),
              Column("password", String(300)),
              Column("num_fogons", Integer),
              )

fogons = Table("fogons", meta,
               Column("id", Integer, primary_key=True),
               Column("title", String(150)),
               Column("power", Integer),
               Column("owner_id", Integer, ForeignKey("users.id")),
               )

meta.create_all(engine)