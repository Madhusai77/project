from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import User

@api_view(['POST'])
def register_user(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    referral_code = request.data.get('referral_code')
    
    # Create user
    user = User.objects.create(name=name, email=email, password=password, referral_code=referral_code)
    
    return Response({'user_id': user.id, 'message': 'User registered successfully'})





@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    data = {
        'name': user.name,
        'email': user.email,
        'referral_code': user.referral_code,
        'timestamp': user.timestamp
    }
    return Response(data)
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def referrals(request):
    user = request.user
    referred_users = User.objects.filter(referral_code=user.referral_code)
    # Implement pagination here
    data = [{'name': user.name, 'timestamp': user.timestamp} for user in referred_users]
    return Response(data)
# Inside referrals/views.py



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_details(request):
    """
    Get user details.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Token value
    responses:
      200:
        description: User details retrieved successfully
      401:
        description: Unauthorized
    """
    user = request.user
    data = {
        'name': user.name,
        'email': user.email,
        'referral_code': user.referral_code,
        'timestamp': user.timestamp
    }
    return Response(data)





