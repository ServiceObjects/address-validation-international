using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.Text;
using System.Threading.Tasks;

namespace address_validation_international_dot_net.REST
{/// <summary>
 /// Response from the AVI API
 /// </summary>
    public class AddressInfoResponse 
    {
        public AddressInfo AddressInfo { get; set; }
        public Error Error { get; set; }
        public override string ToString()
        {
            return $"AVI Response: " +
                $"\nAddressInfo: {AddressInfo} " +
                $"\nError: {{{Error}}}";
        }
    }
    /// <summary>
    /// Information on each address
    /// </summary>
    public class AddressInfo
    {
        public string Status { get; set; }
        public string ResolutionLevel { get; set; }
        public string Address1 { get; set; }
        public string Address2 { get; set; }
        public string Address3 { get; set; }
        public string Address4 { get; set; }
        public string Address5 { get; set; }
        public string Address6 { get; set; }
        public string Address7 { get; set; }
        public string Address8 { get; set; }
        public string Locality { get; set; }
        public string AdministrativeArea { get; set; }
        public string PostalCode { get; set; }
        public string Country { get; set; }
        public string CountryISO2 { get; set; }
        public string CountryISO3 { get; set; }
        public InformationComponent[] InformationComponents { get; set; }
        public override string ToString()
        {
            return $"\n{{Status: {Status} " +
                $"\nResolutionLevel: {ResolutionLevel} " +
                $"\nAddress1: {Address1} " +
                $"\nAddress2: {Address2} " +
                $"\nAddress2: {Address3} " +
                $"\nAddress4: {Address4} " +
                $"\nAddress5: {Address5} " +
                $"\nAddress6: {Address6} " +
                $"\nAddress7: {Address7} " +
                $"\nAddress8: {Address8} " +
                $"\nLocality: {Locality} " +
                $"\nAdministrativeArea: {AdministrativeArea} " +
                $"\nPostalCode: {PostalCode} " +
                $"\nCountry: {Country} " +
                $"\nCountryISO2: {CountryISO2} " +
                $"\nCountryISO3: {CountryISO3} " +
                $"\nInformationComponents: {InformationComponents}}}\n";
        }

    }
    public class InformationComponent
    {
        public string Name { get; set; }
        public string Value { get; set; }
        public override string ToString()
        {
            return $"Name: {Name} " +
                $"\nValue: {Value}\n";
        }
    }

    public class Error
    {
        public string Type { get; set; }
        public string TypeCode { get; set; }
        public string Desc { get; set; }
        public string DescCode { get; set; }
        public override string ToString()
        {
            return $"Type: {Type} " +
                $"\nTypeCode: {TypeCode} " +
                $"\nDesc: {Desc} " +
                $"\nDescCode: {DescCode} ";
        }
    }

}
