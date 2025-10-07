import sys
import os

sys.path.insert(0, os.path.abspath("../address-validation-international-python/SOAP"))

from get_address_info_soap import GetAddressInfoSoap

def get_address_info_soap_sdk_go(is_live: bool, license_key: str) -> None:
   
    print("\r\n------------------------------------------------------------")
    print("Address Validation International - GetAddressInfo - SOAP SDK")
    print("------------------------------------------------------------")

    address1 = "27 E Cota St"
    address2 = "Ste 500"
    address3 = ""
    address4 = ""
    address5 = ""
    locality = "Santa Barbara"
    administrative_area = "CA"
    postal_code = "93101"
    country = "USA"
    output_language = "English"
    timeout_seconds = 15

    print("\r\n* Input *\r\n")
    print(f"Address1          : {address1}")
    print(f"Address2          : {address2}")
    print(f"Address3          : {address3}")
    print(f"Address4          : {address4}")
    print(f"Address5          : {address5}")
    print(f"Locality          : {locality}")
    print(f"AdministrativeArea: {administrative_area}")
    print(f"PostalCode        : {postal_code}")
    print(f"Country           : {country}")
    print(f"OutputLanguage    : {output_language}")
    print(f"License Key       : {license_key}")
    print(f"Is Live           : {is_live}")
    print(f"Timeout Seconds   : {timeout_seconds}")

    try:
        service = GetAddressInfoSoap(license_key, is_live, timeout_seconds * 1000)
        response = service.get_address_info(
            address1,
            address2,
            address3,
            address4,
            address5,
            locality,
            administrative_area,
            postal_code,
            country,
            output_language
        )

        if not hasattr(response, 'Error') or not response.Error:
            print("\r\n* Address Info *\r\n")
            if hasattr(response, 'AddressInfo') and response.AddressInfo:
                print(f"Status            : {getattr(response.AddressInfo, 'Status', None)}")
                print(f"ResolutionLevel   : {getattr(response.AddressInfo, 'ResolutionLevel', None)}")
                print(f"Address1          : {getattr(response.AddressInfo, 'Address1', None)}")
                print(f"Address2          : {getattr(response.AddressInfo, 'Address2', None)}")
                print(f"Address3          : {getattr(response.AddressInfo, 'Address3', None)}")
                print(f"Address4          : {getattr(response.AddressInfo, 'Address4', None)}")
                print(f"Address5          : {getattr(response.AddressInfo, 'Address5', None)}")
                print(f"Address6          : {getattr(response.AddressInfo, 'Address6', None)}")
                print(f"Address7          : {getattr(response.AddressInfo, 'Address7', None)}")
                print(f"Address8          : {getattr(response.AddressInfo, 'Address8', None)}")
                print(f"Locality          : {getattr(response.AddressInfo, 'Locality', None)}")
                print(f"AdministrativeArea: {getattr(response.AddressInfo, 'AdministrativeArea', None)}")
                print(f"PostalCode        : {getattr(response.AddressInfo, 'PostalCode', None)}")
                print(f"Country           : {getattr(response.AddressInfo, 'Country', None)}")
                print(f"CountryISO2       : {getattr(response.AddressInfo, 'CountryISO2', None)}")
                print(f"CountryISO3       : {getattr(response.AddressInfo, 'CountryISO3', None)}")

                print("\r\n* Information Components *\r\n")
                if hasattr(response.AddressInfo, 'InformationComponents') and response.AddressInfo.InformationComponents:
                    components = response.AddressInfo.InformationComponents.InformationComponent
                    if not isinstance(components, list):
                        components = [components]
                    for component in components:
                        print(f"{getattr(component, 'Name', None)}: {getattr(component, 'Value', None)}")
                else:
                    print("No information components found.")
            else:
                print("No address info found.")
        else:
            print("No address info found.")

        if hasattr(response, 'Error') and response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type    : {getattr(response.Error, 'Type', None)}")
            print(f"Error TypeCode: {getattr(response.Error, 'TypeCode', None)}")
            print(f"Error Desc    : {getattr(response.Error, 'Desc', None)}")
            print(f"Error DescCode: {getattr(response.Error, 'DescCode', None)}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Exception occurred: {str(e)}")