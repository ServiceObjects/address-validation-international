from avi_response import AddressInfoResponse, AddressInfo, InformationComponent, Error
import requests

# Endpoint URLs for ServiceObjects Address Validation International (AVI) API
primary_url = "https://sws.serviceobjects.com/avi/api.svc/json/GetAddressInfo?"
backup_url = "https://swsbackup.serviceobjects.com/avi/api.svc/json/GetAddressInfo?"
trial_url = "https://trial.serviceobjects.com/avi/api.svc/json/GetAddressInfo?"

def get_address_info(
    address1: str,
    address2: str,
    address3: str,
    address4: str,
    address5: str,
    locality: str,
    administrative_area: str,
    postal_code: str,
    country: str,
    output_language: str,
    license_key: str,
    is_live: bool = True
) -> AddressInfoResponse:
    """
    Call ServiceObjects Address Validation International (AVI) API's GetAddressInfo endpoint
    to retrieve validated and corrected international address information.

    Parameters:
        address1: Address line 1 of the international address.
        address2: Address line 2 of the international address. Optional.
        address3: Address line 3 of the international address. Optional.
        address4: Address line 4 of the international address. Optional.
        address5: Address line 5 of the international address. Optional.
        locality: The city, town, or municipality of the address. Required if postal code is not provided.
        administrative_area: The state, region, or province of the address. Required if postal code is not provided.
        postal_code: The postal code of the address. Required if locality and administrative area are not provided.
        country: The country name or ISO 3166-1 Alpha-2/Alpha-3 code.
        output_language: The language for service output (e.g., "ENGLISH", "BOTH", "LOCAL_ROMAN", "LOCAL").
        license_key: Your ServiceObjects license key.
        is_live: Use live or trial servers.

    Returns:
        AddressInfoResponse: Parsed JSON response with validated address details or error details.

    Raises:
        RuntimeError: If the API returns an error payload.
        requests.RequestException: On network/HTTP failures (trial mode).
    """
    params = {
        "Address1": address1,
        "Address2": address2,
        "Address3": address3,
        "Address4": address4,
        "Address5": address5,
        "Locality": locality,
        "AdministrativeArea": administrative_area,
        "PostalCode": postal_code,
        "Country": country,
        "OutputLanguage": output_language,
        "LicenseKey": license_key,
    }
    # Select the base URL: production vs trial
    url = primary_url if is_live else trial_url

    try:
        # Attempt primary (or trial) endpoint
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # If API returned an error in JSON payload, trigger fallback
        error = data.get('Error')
        if not (error is None or error.get('TypeCode') != "3"):
            if is_live:
                # Try backup URL
                response = requests.get(backup_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()

                # If still error, propagate exception
                if 'Error' in data:
                    raise RuntimeError(f"AVI service error: {data['Error']}")
            else:
                # Trial mode error is terminal
                raise RuntimeError(f"AVI trial error: {data['Error']}")

        # Convert JSON response to AddressInfoResponse for structured access
        error = Error(**data.get("Error", {})) if data.get("Error") else None
        address_info = data.get("AddressInfo")
        address_info_obj = None
        if address_info:
            address_info_obj = AddressInfo(
                Status=address_info.get("Status"),
                ResolutionLevel=address_info.get("ResolutionLevel"),
                Address1=address_info.get("Address1"),
                Address2=address_info.get("Address2"),
                Address3=address_info.get("Address3"),
                Address4=address_info.get("Address4"),
                Address5=address_info.get("Address5"),
                Address6=address_info.get("Address6"),
                Address7=address_info.get("Address7"),
                Address8=address_info.get("Address8"),
                Locality=address_info.get("Locality"),
                AdministrativeArea=address_info.get("AdministrativeArea"),
                PostalCode=address_info.get("PostalCode"),
                Country=address_info.get("Country"),
                CountryISO2=address_info.get("CountryISO2"),
                CountryISO3=address_info.get("CountryISO3"),
                InformationComponents=[
                    InformationComponent(Name=comp.get("Name"), Value=comp.get("Value"))
                    for comp in address_info.get("InformationComponents", [])
                ] if "InformationComponents" in address_info else []
            )

        return AddressInfoResponse(
            AddressInfo=address_info_obj,
            Error=error
        )

    except requests.RequestException as req_exc:
        # Network or HTTP-level error occurred
        if is_live:
            try:
                # Fallback to backup URL
                response = requests.get(backup_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                if "Error" in data:
                    raise RuntimeError(f"AVI backup error: {data['Error']}") from req_exc

                error = Error(**data.get("Error", {})) if data.get("Error") else None
                address_info = data.get("AddressInfo")
                address_info_obj = None
                if address_info:
                    address_info_obj = AddressInfo(
                        Status=address_info.get("Status"),
                        ResolutionLevel=address_info.get("ResolutionLevel"),
                        Address1=address_info.get("Address1"),
                        Address2=address_info.get("Address2"),
                        Address3=address_info.get("Address3"),
                        Address4=address_info.get("Address4"),
                        Address5=address_info.get("Address5"),
                        Address6=address_info.get("Address6"),
                        Address7=address_info.get("Address7"),
                        Address8=address_info.get("Address8"),
                        Locality=address_info.get("Locality"),
                        AdministrativeArea=address_info.get("AdministrativeArea"),
                        PostalCode=address_info.get("PostalCode"),
                        Country=address_info.get("Country"),
                        CountryISO2=address_info.get("CountryISO2"),
                        CountryISO3=address_info.get("CountryISO3"),
                        InformationComponents=[
                            InformationComponent(Name=comp.get("Name"), Value=comp.get("Value"))
                            for comp in address_info.get("InformationComponents", [])
                        ] if "InformationComponents" in address_info else []
                    )

                return AddressInfoResponse(
                    AddressInfo=address_info_obj,
                    Error=error
                )
            except Exception as backup_exc:
                raise RuntimeError("AVI service unreachable on both endpoints") from backup_exc
        else:
            raise RuntimeError(f"AVI trial error: {str(req_exc)}") from req_exc