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
// 1 Instantiate the service wrapper


// 2 Provide your input data    
//  Fields:
//        Address1
//        Address2
//        Address3
//        Address4
//        Address5
//        PostalCode
//        Locality
//        AdministrativeArea
//        Country
//        OutputLanguage 
//        LicenseKey
//        IsLive

// 3 Call the service

string Address1 = "27 E Cota St";
string Address2 = "Ste 500";
string Address3 = "";
string Address4 = "";
string Address5 = "";
string Locality = "Santa Barbara";
string AdministrativeArea = "CA";
string PostalCode = "93101";
string Country = "USA";
string OutputLanguage = "ENGLISH";
string LicenseKey = "YOUR LICENSE KEY";
bool IsLive = true;

GetAddressInfoValidation avi = new GetAddressInfoValidation(isLive);
AddressInfoResponse response = avi.GetAddressInfo(
    Address1, Address2, Address3, Address4, Address5, Locality, AdministrativeArea, PostalCode, Country, OutputLanguage, LicenseKey).Result;

// 4. Inspect results.
if (response.Error is null)
{
    Console.WriteLine("\r\n* Address Info *\r\n");
    Console.WriteLine($"Status            : {response.AddressInfo?.Status}");
    Console.WriteLine($"ResolutionLevel   : {response.AddressInfo?.ResolutionLevel}");
    Console.WriteLine($"Address1          : {response.AddressInfo?.Address1}");
    Console.WriteLine($"Address2          : {response.AddressInfo?.Address2}");
    Console.WriteLine($"Address3          : {response.AddressInfo?.Address3}");
    Console.WriteLine($"Address4          : {response.AddressInfo?.Address4}");
    Console.WriteLine($"Address5          : {response.AddressInfo?.Address5}");
    Console.WriteLine($"Address6          : {response.AddressInfo?.Address6}");
    Console.WriteLine($"Address7          : {response.AddressInfo?.Address7}");
    Console.WriteLine($"Address8          : {response.AddressInfo?.Address8}");
    Console.WriteLine($"Locality          : {response.AddressInfo?.Locality}");
    Console.WriteLine($"AdministrativeArea: {response.AddressInfo?.AdministrativeArea}");
    Console.WriteLine($"PostalCode        : {response.AddressInfo?.PostalCode}");
    Console.WriteLine($"Country           : {response.AddressInfo?.Country}");
    Console.WriteLine($"CountryISO2       : {response.AddressInfo?.CountryISO2}");
    Console.WriteLine($"CountryISO3       : {response.AddressInfo?.CountryISO3}");

    Console.WriteLine("\r\n* Information Components *\r\n");
    if (response.AddressInfo?.InformationComponents?.Length > 0)
    {
        foreach (InformationComponent component in response.AddressInfo.InformationComponents)
        {
            Console.WriteLine($"{component.Name}: {component.Value}");
        }
    }
    else
    {
        Console.WriteLine("No information components found.");
    }
}
else
{
    Console.WriteLine("\r\n* Error *\r\n");
    Console.WriteLine($"Error Type    : {response.Error.Type}");
    Console.WriteLine($"Error TypeCode: {response.Error.TypeCode}");
    Console.WriteLine($"Error Desc    : {response.Error.Desc}");
    Console.WriteLine($"Error DescCode: {response.Error.DescCode}");
}
```
