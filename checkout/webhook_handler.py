from django.http import HttpResponse


class stripeWH_Handler:
    """handle stripe webhooks""""
    def __init__(self, request):
        self.request = request

    def handle_event(self, request):
        return HttpResponse(
            content=f'webhook recieved: {event["type"]}',
            status=200)
