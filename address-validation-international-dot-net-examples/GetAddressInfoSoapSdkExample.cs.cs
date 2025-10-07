using AVIReference;
using address_validation_international_dot_net.SOAP;

namespace address_validation_international_dot_net_examples
{
    public static class GetAddressInfoSoapSdkExample
    {
        public static void Go(string licenseKey, bool isLive)
        {
            Console.WriteLine("\r\n------------------------------------------------------------");
            Console.WriteLine("Address Validation International - GetAddressInfo - SOAP SDK");
            Console.WriteLine("------------------------------------------------------------");

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

            Console.WriteLine("\r\n* Input *\r\n");
            Console.WriteLine($"Address1          : {Address1}");
            Console.WriteLine($"Address2          : {Address2}");
            Console.WriteLine($"Address3          : {Address3}");
            Console.WriteLine($"Address4          : {Address4}");
            Console.WriteLine($"Address5          : {Address5}");
            Console.WriteLine($"Locality          : {Locality}");
            Console.WriteLine($"AdministrativeArea: {AdministrativeArea}");
            Console.WriteLine($"PostalCode        : {PostalCode}");
            Console.WriteLine($"Country           : {Country}");
            Console.WriteLine($"OutputLanguage    : {OutputLanguage}");
            Console.WriteLine($"LicenseKey        : {licenseKey}");
            Console.WriteLine($"IsLive            : {isLive}");

            GetAddressInfoValidation avi = new GetAddressInfoValidation(isLive);
            AddressInfoResponse response = avi.GetAddressInfo(
                Address1, Address2, Address3, Address4, Address5, Locality, AdministrativeArea, PostalCode, Country, OutputLanguage, licenseKey).Result;

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
        }
    }
}