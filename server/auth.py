import secrets
import sqlite3
import appconfig

def create_token(access):
	token = {'X-KEY-X': secrets.token_urlsafe(16), 'access_level': access}
	_conn = sqlite3.connect(appconfig.sql['name'])
	cur = _conn.cursor()
	cur.execute('INSERT INTO '+ appconfig.sql['access'] +' VALUES ("' + token['X-KEY-X'] + '", "' + token['access_level'] + '");')
	_conn.commit()
	_conn.close()
	return token

def check_token(token):
	_conn = sqlite3.connect(appconfig.sql['name'])
	cur = _conn.cursor()
	cur.execute("SELECT * FROM "+ appconfig.sql['access'] + ";")
	valid_tokens = [i[0] for i in cur.fetchall()]
	_conn.close()
	if token in valid_tokens:
		return True
	else:
		return False