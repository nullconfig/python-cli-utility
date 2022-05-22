import json, requests
import logging
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GithubApiBot(object):
  '''
  GithubApiBot
  '''
  def __init__(self, username):
    self.username = username

  def github_user(self) -> json:
    ''' Takes the username passed in at instantiation, and returns all of the repos found. '''
    return json.dumps(requests.get(f"https://api.github.com/users/{self.username}/repos").json())

