/**
 * Input parameters for the GetAddressInfo API call.
 */
export class GetAddressInfoInput {
    constructor(data = {}) {
        this.Address1 = data.Address1;
        this.Address2 = data.Address2;
        this.Address3 = data.Address3;
        this.Address4 = data.Address4;
        this.Address5 = data.Address5;
        this.Locality = data.Locality;
        this.AdministrativeArea = data.AdministrativeArea;
        this.PostalCode = data.PostalCode;
        this.Country = data.Country;
        this.OutputLanguage = data.OutputLanguage || 'ENGLISH';
        this.LicenseKey = data.LicenseKey;
        this.IsLive = data.IsLive !== undefined ? data.IsLive : true;
        this.TimeoutSeconds = data.TimeoutSeconds !== undefined ? data.TimeoutSeconds : 15;
    }

    toString() {
        return `GetAddressInfoInput: Address1 = ${this.Address1}, Address2 = ${this.Address2}, Address3 = ${this.Address3}, Address4 = ${this.Address4}, Address5 = ${this.Address5}, Locality = ${this.Locality}, AdministrativeArea = ${this.AdministrativeArea}, PostalCode = ${this.PostalCode}, Country = ${this.Country}, OutputLanguage = ${this.OutputLanguage}, LicenseKey = ${this.LicenseKey}, IsLive = ${this.IsLive}, TimeoutSeconds = ${this.TimeoutSeconds}`;
    }
}

/**
 * Information Component for API responses.
 */
export class InformationComponent {
    constructor(data = {}) {
        this.Name = data.Name;
        this.Value = data.Value;
    }

    toString() {
        return `Name = ${this.Name}, Value = ${this.Value}`;
    }
}

/**
 * Error object for API responses.
 */
export class Error {
    constructor(data = {}) {
        this.Type = data.Type;
        this.TypeCode = data.TypeCode;
        this.Desc = data.Desc;
        this.DescCode = data.DescCode;
    }

    toString() {
        return `Error: Type = ${this.Type}, TypeCode = ${this.TypeCode}, Desc = ${this.Desc}, DescCode = ${this.DescCode}`;
    }
}

/**
 * Address information for a validated international address.
 */
export class AddressInfo {
    constructor(data = {}) {
        this.Status = data.Status;
        this.ResolutionLevel = data.ResolutionLevel;
        this.Address1 = data.Address1;
        this.Address2 = data.Address2;
        this.Address3 = data.Address3;
        this.Address4 = data.Address4;
        this.Address5 = data.Address5;
        this.Address6 = data.Address6;
        this.Address7 = data.Address7;
        this.Address8 = data.Address8;
        this.Locality = data.Locality;
        this.AdministrativeArea = data.AdministrativeArea;
        this.PostalCode = data.PostalCode;
        this.Country = data.Country;
        this.CountryISO2 = data.CountryISO2;
        this.CountryISO3 = data.CountryISO3;
        this.InformationComponents = (data.InformationComponents || []).map(component => new InformationComponent(component));
    }

    toString() {
        const componentsString = this.InformationComponents.length
            ? this.InformationComponents.map(component => component.toString()).join(', ')
            : 'null';
        return `AddressInfo: Status = ${this.Status}, ResolutionLevel = ${this.ResolutionLevel}, Address1 = ${this.Address1}, Address2 = ${this.Address2}, Address3 = ${this.Address3}, Address4 = ${this.Address4}, Address5 = ${this.Address5}, Address6 = ${this.Address6}, Address7 = ${this.Address7}, Address8 = ${this.Address8}, Locality = ${this.Locality}, AdministrativeArea = ${this.AdministrativeArea}, PostalCode = ${this.PostalCode}, Country = ${this.Country}, CountryISO2 = ${this.CountryISO2}, CountryISO3 = ${this.CountryISO3}, InformationComponents = [${componentsString}]`;
    }
}

/**
 * Response from GetAddressInfo API, containing validated address information.
 */
export class AddressInfoResponse {
    constructor(data = {}) {
        this.AddressInfo = data.AddressInfo ? new AddressInfo(data.AddressInfo) : null;
        this.Error = data.Error ? new Error(data.Error) : null;
    }

    toString() {
        return `AddressInfoResponse: AddressInfo = ${this.AddressInfo ? this.AddressInfo.toString() : 'null'}, Error = ${this.Error ? this.Error.toString() : 'null'}]`;
    }
}

export default AddressInfoResponse;