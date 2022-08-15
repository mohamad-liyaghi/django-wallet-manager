from accounts.models import User


class CardMiddleware():
    '''
        This middleware checks if users balance is not none.
    '''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated and  request.user.balance == None:
            self.request.user.balance = 0
            self.request.user.save()

        response = self.get_response(request)
        return response

        
