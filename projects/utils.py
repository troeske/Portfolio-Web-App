from .models import Client

def client_approved(user):
    """
    see if a client/user has been approved
    """
    client = Client.objects.filter(client=user).first()
    if client is None:
        return False
    else:
        return client.approved

def not_in_clients(user):
    """
    see if a client/user is in the client list
    """
    client = Client.objects.filter(client=user).first()
    if client is None:
        return True
    else:
        return False