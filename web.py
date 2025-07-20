from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://kick.com/brutalles"
    sb.uc_open_with_reconnect(url, 5)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.uc_gui_handle_captcha()
    
    di2 = sb.get_new_driver(undetectable=True)
    sb.uc_open_with_reconnect(url, 5)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.uc_gui_handle_captcha()

    while(sb.is_element_present('video#video-player')):
        sb.sleep(10)
