
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class GetAddressInfoInput:
    Address1: Optional[str] = None
    Address2: Optional[str] = None
    Address3: Optional[str] = None
    Address4: Optional[str] = None
    Address5: Optional[str] = None
    Locality: Optional[str] = None
    AdministrativeArea: Optional[str] = None
    PostalCode: Optional[str] = None
    Country: Optional[str] = None
    OutputLanguage: str = "ENGLISH"
    LicenseKey: Optional[str] = None
    IsLive: bool = True
    TimeoutSeconds: int = 15

    def __str__(self) -> str:
        return (f"GetAddressInfoInput: Address1={self.Address1}, Address2={self.Address2}, Address3={self.Address3}, "
                f"Address4={self.Address4}, Address5={self.Address5}, Locality={self.Locality}, "
                f"AdministrativeArea={self.AdministrativeArea}, PostalCode={self.PostalCode}, "
                f"Country={self.Country}, OutputLanguage={self.OutputLanguage}, LicenseKey={self.LicenseKey}, "
                f"IsLive={self.IsLive}, TimeoutSeconds={self.TimeoutSeconds}")


@dataclass
class InformationComponent:
    Name: Optional[str] = None
    Value: Optional[str] = None

    def __str__(self) -> str:
        return f"InformationComponent: Name={self.Name}, Value={self.Value}"


@dataclass
class Error:
    Type: Optional[str] = None
    TypeCode: Optional[str] = None
    Desc: Optional[str] = None
    DescCode: Optional[str] = None

    def __str__(self) -> str:
        return f"Error: Type={self.Type}, TypeCode={self.TypeCode}, Desc={self.Desc}, DescCode={self.DescCode}"


@dataclass
class AddressInfo:
    Status: Optional[str] = None
    ResolutionLevel: Optional[str] = None
    Address1: Optional[str] = None
    Address2: Optional[str] = None
    Address3: Optional[str] = None
    Address4: Optional[str] = None
    Address5: Optional[str] = None
    Address6: Optional[str] = None
    Address7: Optional[str] = None
    Address8: Optional[str] = None
    Locality: Optional[str] = None
    AdministrativeArea: Optional[str] = None
    PostalCode: Optional[str] = None
    Country: Optional[str] = None
    CountryISO2: Optional[str] = None
    CountryISO3: Optional[str] = None
    InformationComponents: Optional[List['InformationComponent']] = None

    def __post_init__(self):
        if self.InformationComponents is None:
            self.InformationComponents = []

    def __str__(self) -> str:
        components_string = ', '.join(str(component) for component in self.InformationComponents) if self.InformationComponents else 'None'
        return (f"AddressInfo: Status={self.Status}, ResolutionLevel={self.ResolutionLevel}, "
                f"Address1={self.Address1}, Address2={self.Address2}, Address3={self.Address3}, "
                f"Address4={self.Address4}, Address5={self.Address5}, Address6={self.Address6}, "
                f"Address7={self.Address7}, Address8={self.Address8}, Locality={self.Locality}, "
                f"AdministrativeArea={self.AdministrativeArea}, PostalCode={self.PostalCode}, "
                f"Country={self.Country}, CountryISO2={self.CountryISO2}, CountryISO3={self.CountryISO3}, "
                f"InformationComponents=[{components_string}]")


@dataclass
class AddressInfoResponse:
    AddressInfo: Optional['AddressInfo'] = None
    Error: Optional['Error'] = None

    def __str__(self) -> str:
        address_info_string = str(self.AddressInfo) if self.AddressInfo else 'None'
        error_string = str(self.Error) if self.Error else 'None'
        return (f"AddressInfoResponse: AddressInfo={address_info_string}, "
                f"Error={error_string}]")