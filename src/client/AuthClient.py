import requests


class AuthClient:
    def __init__(self, api_key, base_url="https://auth.lumaserv.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer ' + . api_key,
            'Content-Type': 'application/json'
        })

    def request(self, method, path, params={}, body={}):
        r = self.session.request(method, self.base_url + path, data=data, params=params)
        f(r.status_code < 200 or (r.status_code >= 300 and r.status_code < 400):
            raise Exception("Status code is " + r.status_code + "!")
        return r.json()

    def createProject(self, body, queryParams={}):
        return self.request("POST", "/projects".format(), queryParams, body);


    def getProjects(self, queryParams={}):
        return self.request("GET", "/projects".format(), queryParams);


    def getProject(self, id, queryParams={}):
        return self.request("GET", "/projects/{id}".format(id=id), queryParams);


    def deleteProject(self, id, queryParams={}):
        return self.request("DELETE", "/projects/{id}".format(id=id), queryParams);


    def updateProject(self, id, body, queryParams={}):
        return self.request("PUT", "/projects/{id}".format(id=id), queryParams, body);


    def login(self, body, queryParams={}):
        return self.request("POST", "/login".format(), queryParams, body);


    def createUser(self, body, queryParams={}):
        return self.request("POST", "/users".format(), queryParams, body);


    def getUsers(self, queryParams={}):
        return self.request("GET", "/users".format(), queryParams);


    def getUser(self, id, queryParams={}):
        return self.request("GET", "/users/{id}".format(id=id), queryParams);


    def updateUser(self, id, body, queryParams={}):
        return self.request("PUT", "/users/{id}".format(id=id), queryParams, body);


    def requestPasswordReset(self, body, queryParams={}):
        return self.request("POST", "/password-reset".format(), queryParams, body);


    def executePasswordReset(self, body, queryParams={}):
        return self.request("PUT", "/password-reset".format(), queryParams, body);


    def insertAuditLogEntry(self, body, queryParams={}):
        return self.request("POST", "/audit-log".format(), queryParams, body);


    def searchAuditLog(self, queryParams={}):
        return self.request("GET", "/audit-log".format(), queryParams);


    def createToken(self, body, queryParams={}):
        return self.request("POST", "/tokens".format(), queryParams, body);


    def getTokens(self, queryParams={}):
        return self.request("GET", "/tokens".format(), queryParams);


    def getCountry(self, code, queryParams={}):
        return self.request("GET", "/countries/{code}".format(code=code), queryParams);


    def getToken(self, id, queryParams={}):
        return self.request("GET", "/tokens/{id}".format(id=id), queryParams);


    def deleteToken(self, id, queryParams={}):
        return self.request("DELETE", "/tokens/{id}".format(id=id), queryParams);


    def validateToken(self, token, queryParams={}):
        return self.request("GET", "/validate/{token}".format(token=token), queryParams);


    def addProjectMember(self, id, body, queryParams={}):
        return self.request("POST", "/projects/{id}/members".format(id=id), queryParams, body);


    def getProjectMembers(self, id, queryParams={}):
        return self.request("GET", "/projects/{id}/members".format(id=id), queryParams);


    def searchTransactionLog(self, body, queryParams={}):
        return self.request("POST", "/transaction-log".format(), queryParams, body);


    def validateSelf(self, queryParams={}):
        return self.request("GET", "/validate/self".format(), queryParams);


    def removeProjectMember(self, id, user_id, queryParams={}):
        return self.request("DELETE", "/projects/{id}/members/{user_id}".format(id=id, user_id=user_id), queryParams);


    def getUserProjectMemberships(self, id, queryParams={}):
        return self.request("GET", "/users/{id}/project_memberships".format(id=id), queryParams);


    def getCountries(self, queryParams={}):
        return self.request("GET", "/countries".format(), queryParams);


