import os
import ast


INSTAGRAM_CUSTOM_USER_HEADER: dict = ast.literal_eval(
    os.environ.get(
        'INSTAGRAM_CUSTOM_USER_HEADER',
        """{'x-csrftoken': 'qrY8EGVuYtCUNgRSF7Hy17m765vM6frX','x-ig-www-claim': 'hmac.AR1rphEFZb1iYo4xXaf90ZcwS6YP_RiJAkxlPf_jC1_Bd1X7','x-asbd-id': '129477','x-ig-app-id': '936619743392459',}"""
    ),
)
# You can save it in the database and update it manually or put a crawler to update it.
