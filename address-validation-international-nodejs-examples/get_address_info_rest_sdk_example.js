import { GetAddressInfoClient } from '../address-validation-international-nodejs/REST/get_address_info_rest.js';

async function GetAddressInfoRestGo(licenseKey, isLive) {
    console.log("\n------------------------------------------------------------");
    console.log("Address Validation International - GetAddressInfo - REST SDK");
    console.log("------------------------------------------------------------");

    const address1 = "27 E Cota St";
    const address2 = "Ste 500";
    const address3 = "";
    const address4 = "";
    const address5 = "";
    const locality = "Santa Barbara";
    const administrativeArea = "CA";
    const postalCode = "93101";
    const country = "USA";
    const outputLanguage = "English";
    const timeoutSeconds = 15;

    console.log("\n* Input *\n");
    console.log(`Address1          : ${address1}`);
    console.log(`Address2          : ${address2}`);
    console.log(`Address3          : ${address3}`);
    console.log(`Address4          : ${address4}`);
    console.log(`Address5          : ${address5}`);
    console.log(`Locality          : ${locality}`);
    console.log(`AdministrativeArea: ${administrativeArea}`);
    console.log(`PostalCode        : ${postalCode}`);
    console.log(`Country           : ${country}`);
    console.log(`OutputLanguage    : ${outputLanguage}`);
    console.log(`License Key       : ${licenseKey}`);
    console.log(`Is Live           : ${isLive}`);
    console.log(`Timeout Seconds   : ${timeoutSeconds}`);

    try {
        const response = await GetAddressInfoClient.invoke(
            address1,
            address2,
            address3,
            address4,
            address5,
            locality,
            administrativeArea,
            postalCode,
            country,
            outputLanguage,
            licenseKey,
            isLive,
            timeoutSeconds
        );

        if (response.Error) {
            console.log("\n* Error *\n");
            console.log(`Error Type    : ${response.Error.Type}`);
            console.log(`Error TypeCode: ${response.Error.TypeCode}`);
            console.log(`Error Desc    : ${response.Error.Desc}`);
            console.log(`Error DescCode: ${response.Error.DescCode}`);
            return;
        }

        console.log("\n* Address Info *\n");
        if (response && response.AddressInfo) {
            console.log(`Status            : ${response.AddressInfo.Status}`);
            console.log(`ResolutionLevel   : ${response.AddressInfo.ResolutionLevel}`);
            console.log(`Address1          : ${response.AddressInfo.Address1}`);
            console.log(`Address2          : ${response.AddressInfo.Address2}`);
            console.log(`Address3          : ${response.AddressInfo.Address3}`);
            console.log(`Address4          : ${response.AddressInfo.Address4}`);
            console.log(`Address5          : ${response.AddressInfo.Address5}`);
            console.log(`Address6          : ${response.AddressInfo.Address6}`);
            console.log(`Address7          : ${response.AddressInfo.Address7}`);
            console.log(`Address8          : ${response.AddressInfo.Address8}`);
            console.log(`Locality          : ${response.AddressInfo.Locality}`);
            console.log(`AdministrativeArea: ${response.AddressInfo.AdministrativeArea}`);
            console.log(`PostalCode        : ${response.AddressInfo.PostalCode}`);
            console.log(`Country           : ${response.AddressInfo.Country}`);
            console.log(`CountryISO2       : ${response.AddressInfo.CountryISO2}`);
            console.log(`CountryISO3       : ${response.AddressInfo.CountryISO3}`);

            console.log("\n* Information Components *\n");
            if (response.AddressInfo.InformationComponents && response.AddressInfo.InformationComponents.length > 0) {
                response.AddressInfo.InformationComponents.forEach((component) => {
                    console.log(`${component.Name}: ${component.Value}`);
                });
            } else {
                console.log("No information components found.");
            }
        } else {
            console.log("No address info found.");
        }
    } catch (e) {
        console.log("\n* Error *\n");
        console.log(`Error Message: ${e.message}`);
    }
}

export { GetAddressInfoRestGo };