# from django.contrib.auth import get_user_model, authenticate
# from django.contrib.auth.backends import ModelBackend
# from dap.models import Reg_User as ru


# user = authenticate(username = ru.objects.get(username = 'SELECT * FROM public.dap_reg_user WHERE username = username AND password = password'))

# if user is not None:

# else:

# class CaseInsensitiveModelBackend(ModelBackend):
# 	"""docstring for CaseInsensitiveModelBackend"""
# 	def authenticate(self, request, username=None, password = None, **kwargs):
# 		UserModel = get_user_model()

# 		if username is None:
# 			username = kwargs.get(UserModel.USERNAME_FIELD)

# 		try:
# 			case_insensitive_username_field = '{}__iexact'.format(userModel.USERNAME_FIELD)
# 			user = UserModel._default_manager.get(**{case_insensitive_username_field:username})



# 		except UserModel.DoesNotExist:
# 			UserModel().set_password(password)
		
# 		else:
# 			if user.check_password(password) and self.user_can_authenticate(user):
# 				return user


