![Service Objects Logo](https://www.serviceobjects.com/wp-content/uploads/2021/05/SO-Logo-with-TM.gif "Service Objects Logo")

# AVI - Address Validation International

DOTS Address Validation International (AVI) can be used as a RESTful service or with SOAP. AVI is designed to take an international address, validate it and return a standardized international version of the address. Depending on the information available for a given address, AVI can return additional information about a given address. For example, it can return Delivery Point Validation (DPV) information for US addresses.

AVI can provide instant address verification and correction to websites or enhancement to contact lists. However, the output from AVI must be considered carefully before the existence or non-existence of an address is decided

## [Service Objects Website](https://serviceobjects.com)

# AVI - GetAddressInfo

Our real-time International Address Validation API service verifies and corrects global mailing addresses to the unique requirements of each country’s postal address formats and cultural idiosyncrasies. 

With continual updates from country-specific postal authorities, our data is always up-to-date with genuine and accurate addresses.

### [GetAddressInfo Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-address-validation-international/avi-operations/avi-getaddressinfo-recommended/)

## Library Usage

```
// 1. Build the input
//
//  Fields:
//        address1
//        address2
//        address3
//        address4
//        address5
//        locality
//        administrative_area
//        postal_code
//        country
//        output_language 
//        license_key
//        is_live 

from get_address_info_rest import get_address_info

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
is_live = True
license_key = "YOUR LICENSE KEY"

// 2. Call the method.
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

// 3. Inspect results.
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
```
