import  ipinfo, random, requests

from django.conf                                                        import settings


def get_user_ip_data(remote_ip):

    ipinfo_data  = {
        'ip'            : '154.73.22.46',
        'city'          : 'Kinshasa',
        'postal'        : '',
        'region'        : 'Kinshasa',
        'country'       : 'CD',
        'loc'           : '-4.3276,15.3136',
        'org'           : 'AS327738 STE AFRICELL RDC SPRL',
        'timezone'      : 'Africa/Kinshasa',
        'country_name'  : 'Democratic Republic of the Congo',
        'latitude'      : '-4.3276',
        'longitude'     : '15.3136'
    }

    if remote_ip == '154.73.22.46' or remote_ip == '127.0.0.1':
        return ipinfo_data

    try:

        access_token = get_access_token()

        response     = requests.get(f'https://ipinfo.io/{remote_ip}/json?token={access_token}')

        if response.status_code != 200:
            access_token = get_access_token()
            response     = requests.get(f'https://ipinfo.io/{remote_ip}/json?token={access_token}')

            """ -- IF 403 --> CANNOT FIND USER OR USER FORBIDDEN -- """

            """ -- IF 429 --> MONTHLY USAGE EXCEEDED -- """

        if response.status_code == 200:

            ipinfo_data = response.json()

            ipinfo_settings = getattr(settings, "IPINFO_SETTINGS", {})
            ip_data         = ipinfo.getHandler(access_token, **ipinfo_settings)
            ipinfo_data     = ip_data.getDetails(remote_ip).all

    except Exception as e:
        print("Error occured ==> ", e)

    return ipinfo_data


def get_access_token():

    access_token1 = settings.IPINFO_TOKEN_1
    access_token2 = settings.IPINFO_TOKEN_2
    access_token3 = settings.IPINFO_TOKEN_3
    access_token4 = settings.IPINFO_TOKEN_4
    access_token5 = settings.IPINFO_TOKEN_5

    access_tokens = [access_token1, access_token2, access_token3, access_token4, access_token5]
    index_int     = len(access_tokens) - 1
    rand_int      = random.randint(0, index_int)
    access_token  = access_tokens[rand_int]

    return access_token


def create_ip_data_dict(i):

    ip_data = {
        'ip'            : i['ip'],
        'city'          : i['city'],
        'postal'        : '',
        'region'        : i['region'],
        'country'       : i['country'],
        'loc'           : i['loc'],
        'org'           : i['org'],
        'timezone'      : i['timezone'],
        'country_name'  : i['country_name'],
        'latitude'      : i['latitude'],
        'longitude'     : i['longitude'],
    }

    return ip_data
