from model.Account import Account
class User:
    def __init__(self, firstname, lastname, account: Account):
        self._firstname = firstname
        self._lastname = lastname
        if(not isinstance(account, Account)):
            raise TypeError('Invalid account type, must be Account object')
        self._account = account

    
