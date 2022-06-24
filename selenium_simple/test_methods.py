from first_connects import DB

db = DB()

class methods_cl:
	def get_data(self):
		return db.q_new("""SELECT *, cast(СумДоход as int) - cast(СумРасход as int) from dohrash 
				  		   order by (cast(СумДоход as int) - cast(СумРасход as int)) desc 
				  		   limit 25;""")