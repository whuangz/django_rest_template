import json
import auth
from .model import Account, Teacher, AccountOauth
from core.base import session
from core import http_client

class AccountService():
	def create_login(self, param):
		token, error = auth.get_token(param,register=0)
		if not token:
			return None, error

		try:
			account = session.query(Account).join(AccountOauth).filter(AccountOauth.oauth_user_id==token["user_id"]).first()

			if not account:
				return None, {"status_code": 404, "message": "User not found"}

			account.access_token = token['access_token']
			account.refresh_token = token['refresh_token']

			return account, None
		except:
			return None, {"status_code": 404, "message": "User not found"}
		

class TeacherService():
	def create_teacher(self, param):
		token, error = auth.get_token(param, register=1)
		if not token:
			return None, error
		try:
			existing_account = session.query(Account).filter_by(email=param["email"], deleted_at=None).first()
			if existing_account is None:
				account = Account(param)
				session.add(account)
				session.flush()

				body = {
					"account_id": account.id,
					"teaching_field": param["teaching_field"]
				}

				teacher = Teacher(body)
				session.add(teacher)
				
			else:
				session.rollback()
				return None, {"status_code": 409, "message": "User already Exist"}

			#get oauth id
			print(token)
			account_oauth_param = {
				"account_id": account.id,
				"oauth_user_id" : token["user_id"]
			}

			account_oauth = AccountOauth(account_oauth_param)
			session.add(account_oauth)
			session.commit()

		except:
			session.rollback()
			return None, {"status_code": 409, "message": "User already Exist"}

		response = {
			"access_token" : token["access_token"],
			"refresh_token" : token["refresh_token"]
		}

		return response, None