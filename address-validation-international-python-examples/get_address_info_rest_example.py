import sys
import os

sys.path.insert(0, os.path.abspath("../address-validation-international-python/REST"))

from get_address_info_rest import get_address_info

def get_address_info_rest_sdk_go(is_live: bool, license_key: str) -> None:
   
    print("\r\n------------------------------------------------------------")
    print("Address Validation International - GetAddressInfo - REST SDK")
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

    try:
        response = get_address_info(
            address1,
            address2,
            address3,
            address4,
            address5,
            locality,
            administrative_area,
            postal_code,
            country,
            output_language,
            license_key,
            is_live
        )

        print("\r\n* Address Info *\r\n")
        if response and not response.Error and response.AddressInfo:
            print(f"Status            : {response.AddressInfo.Status}")
            print(f"ResolutionLevel   : {response.AddressInfo.ResolutionLevel}")
            print(f"Address1          : {response.AddressInfo.Address1}")
            print(f"Address2          : {response.AddressInfo.Address2}")
            print(f"Address3          : {response.AddressInfo.Address3}")
            print(f"Address4          : {response.AddressInfo.Address4}")
            print(f"Address5          : {response.AddressInfo.Address5}")
            print(f"Address6          : {response.AddressInfo.Address6}")
            print(f"Address7          : {response.AddressInfo.Address7}")
            print(f"Address8          : {response.AddressInfo.Address8}")
            print(f"Locality          : {response.AddressInfo.Locality}")
            print(f"AdministrativeArea: {response.AddressInfo.AdministrativeArea}")
            print(f"PostalCode        : {response.AddressInfo.PostalCode}")
            print(f"Country           : {response.AddressInfo.Country}")
            print(f"CountryISO2       : {response.AddressInfo.CountryISO2}")
            print(f"CountryISO3       : {response.AddressInfo.CountryISO3}")

            print("\r\n* Information Components *\r\n")
            if response.AddressInfo.InformationComponents and len(response.AddressInfo.InformationComponents) > 0:
                for component in response.AddressInfo.InformationComponents:
                    print(f"{component.Name}: {component.Value}")
            else:
                print("No information components found.")
        else:
            print("No address info found.")

        if response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type    : {response.Error.Type}")
            print(f"Error TypeCode: {response.Error.TypeCode}")
            print(f"Error Desc    : {response.Error.Desc}")
            print(f"Error DescCode: {response.Error.DescCode}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Error Message: {str(e)}")