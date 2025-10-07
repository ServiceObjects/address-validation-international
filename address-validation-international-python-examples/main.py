from get_address_info_rest_example import get_address_info_rest_sdk_go
from get_address_info_soap_example import get_address_info_soap_sdk_go

if __name__ =="__main__":

    # Your license key from Service Objects.  
    # Trial license keys will only work on the trial environments and production  
    # license keys will only work on production environments.
    #   
    license_key = "LICENSE KEY"  
    is_live = True

    # Address Validation International - GetAddressInfo - REST SDK
    get_address_info_rest_sdk_go(is_live, license_key)

    # Address Validation International - GetAddressInfo - SOAP SDK
    get_address_info_soap_sdk_go(is_live, license_key)
