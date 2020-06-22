from sqlalchemy import create_engine, select, MetaData, Table,update
from sqlalchemy.sql import and_, or_,exists

from core import config

engine = create_engine(config['DATABASE_URI'])

class UserModel():

	def __init__(self):
		try:
			self.meta = MetaData()
			self.users = Table("users", self.meta, autoload=True, autoload_with=engine)
		except Exception as e:
			print(e)

	def create(self,data):
 		result = engine.execute(self.users.insert(), data)
 		return result.inserted_primary_key
 		
		
	# def create(self,data):
 	# 	stmt = engine.execute(self.users.insert(), data)
 	# 	stmt = select([self.users])
	# 	# stmt = stmt.where(
 	# 	# 		self.users.c.mobile.in_([new_dict])
	# 	# 	)
 	# 	result = engine.execute(stmt)
 	# 	temp = [dict(r) for r in result] if result else None
 	# 	print(temp)
 	# 	return temp	

	def get(self,id):
		stmt = select([self.users])			
		stmt = stmt.where(
 				self.users.c.user_id.in_([id])
			)
		result = engine.execute(stmt)					
		temp = [dict(r) for r in result] if result else None
		return temp


	def checkmobile(self,new_dict):
 		stmt = select([self.users])
 		stmt = stmt.where(
 				self.users.c.mobile.in_([new_dict])
			)
 		result = engine.execute(stmt)
 		temp = [dict(r) for r in result] if result else None
 		print(temp)
 		return temp

		
	
	def check(self,new_dict):
 		stmt = select([self.users])
 		stmt = stmt.where(
 				self.users.c.mobile.in_([new_dict])
			)
 		result = engine.execute(stmt)
 		temp = [dict(r) for r in result] if result else None
 		print(temp)
 		return temp	
	
	def update(self,data,id):
 		stmt = self.users.update()
 		stmt =stmt.where(
 				self.users.c.user_id.in_([id]))
 		result=engine.execute(stmt,data)
 		return result.rowcount

 		

		
	    

		
	
		
