from suds.client import Client
from suds import WebFault
from suds.sudsobject import Object

class GetAddressInfoSoap:
    def __init__(self, license_key: str, is_live: bool = True, timeout_ms: int = 15000):
        """
        license_key: Service Objects AVI license key.
        is_live: Whether to use live or trial endpoints.
        timeout_ms: SOAP call timeout in milliseconds.
        """
        self.is_live = is_live
        self.timeout = timeout_ms / 1000.0
        self.license_key = license_key

        # WSDL URLs
        self._primary_wsdl = (
            "https://sws.serviceobjects.com/avi/soap.svc?wsdl"
            if is_live
            else "https://trial.serviceobjects.com/avi/soap.svc?wsdl"
        )
        self._backup_wsdl = (
            "https://swsbackup.serviceobjects.com/avi/soap.svc?wsdl"
            if is_live
            else "https://trial.serviceobjects.com/avi/soap.svc?wsdl"
        )

    def get_address_info(
        self,
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
    ) -> Object:
        """
        Calls the GetAddressInfo SOAP API to retrieve validated and corrected international address information.

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
            is_live: Determines whether to use the live or trial servers.
            timeout_ms: Timeout, in milliseconds, for the call to the service.

        Returns:
            suds.sudsobject.Object: SOAP response containing validated address details or error.

        Raises:
            RuntimeError: If both primary and backup endpoints fail.
        """
        # Common kwargs for both calls
        call_kwargs = dict(
            Address1=address1,
            Address2=address2,
            Address3=address3,
            Address4=address4,
            Address5=address5,
            Locality=locality,
            AdministrativeArea=administrative_area,
            PostalCode=postal_code,
            Country=country,
            OutputLanguage=output_language,
            LicenseKey=self.license_key,
        )

        # Attempt primary
        try:
            client = Client(self._primary_wsdl, timeout=self.timeout)
            # Override endpoint URL if needed:
            # client.set_options(location=self._primary_wsdl.replace('?wsdl','/soap'))
            response = client.service.GetAddressInfo(**call_kwargs)

            # If response invalid or Error.TypeCode == "3", trigger fallback
            if response is None or (
                hasattr(response, "Error")
                and response.Error
                and response.Error.TypeCode == "3"
            ):
                raise ValueError("Primary returned no result or Error.TypeCode=3")

            return response

        except (WebFault, ValueError, Exception) as primary_ex:
            # Attempt backup
            try:
                client = Client(self._backup_wsdl, timeout=self.timeout)
                response = client.service.GetAddressInfo(**call_kwargs)
                if response is None:
                    raise ValueError("Backup returned no result")
                return response
            except (WebFault, Exception) as backup_ex:
                msg = (
                    "Both primary and backup endpoints failed.\n"
                    f"Primary error: {str(primary_ex)}\n"
                    f"Backup error: {str(backup_ex)}"
                )
                raise RuntimeError(msg)