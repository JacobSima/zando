
def get_device_info(request):

    user_agent  = request.user_agent
    device_type = 'Desktop PC'

    if user_agent.is_mobile:
        device_type = 'Mobile Phone'

    if user_agent.is_tablet:
        device_type = 'Tablet'

    # if user_agent.is_pc:
    #     device_type = 'Desktop PC'

    if user_agent.is_touch_capable:
        device_type = 'Touch Screen'

    if user_agent.is_bot:
        device_type = 'Web Crawler - Bot'

    device = {
        'type'              : device_type,
        'model'             : user_agent.device.family,
        'os'                : f"{user_agent.os.family} {user_agent.os.version_string}",
        'os_version'        : f"{user_agent.os.version_string}",
        'browser'           : f"{user_agent.browser.family} {user_agent.browser.version_string}",
        'browser_version'   : f"{user_agent.browser.version_string}",
    }

    return device
