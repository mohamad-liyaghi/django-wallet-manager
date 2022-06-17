from account.models import User


class CardMiddleware():
    '''
        This middleware checks if users fund is not none.
    '''
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):

        if request.user.is_authenticated and  request.user.fund == None:
            User.objects.filter(username=request.user.username).update(fund=0)

        response = self.get_response(request)
        return response

        
