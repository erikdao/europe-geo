type CountryLatLng = {
  country: number[];
  capital: number[];
}

export type Country = {
  name: string;
  official_name: string;
  topLevelDomain: string[];
  alpha2Code: string;
  callingCode: string;
  capital: string;
  population: number;
  area: number;
  currencies?: any;
  languages?: any;
  flag?: string;
  latLng: CountryLatLng;
}