import { useEffect, useState } from 'react'
import { ComposableMap, Geographies, Geography, Marker, ZoomableGroup } from 'react-simple-maps'
import { getCountries } from './services';
import { Country } from './types';

// const geoUrl = 'https://raw.githubusercontent.com/deldersveld/topojson/master/continents/europe.json'
const geoUrl = "https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/TopoJSON/europe.topojson"

const EXCLUDED_ALPHA2CODE = [
  "SJ", "IM", "JE", "GI", "SM", "VA", "AX", "GG", "LI"
];

const TRANASIA = [
  "TR", "GE", "AM", "AZ", "IL"
]

function App() {
  const [countries, setCountries] = useState<Country[]>([]);

  useEffect(() => {
    async function getCountriesFromApi() {
      const data: Country[] = await getCountries();
      const filteredCountries = data.filter(c => EXCLUDED_ALPHA2CODE.indexOf(c.alpha2Code) == -1)
      setCountries(filteredCountries);
    }

    getCountriesFromApi();
  }, []);

  const renderGeography = (geo: any) => {
    if (TRANASIA.indexOf(geo.id) !== -1) return null;
    return (
      <Geography
        key={geo.rsmKey}
        geography={geo}
        paintOrder="stroke fill"
        fill="#dcfce7"
        stroke="#166534"
        strokeLinejoin="bevel"
        strokeWidth={1}
        tabIndex={-1}
        style={{
          default: { outline: "none" },
          hover: { outline: "none", fill: "#bbf7d0" },
          pressed: { outline: "none", fill: "#bbf7d0" }
        }}
      />
    )
  }

  const renderCountryNameMarker = (country: Country) => {
    if (country.alpha2Code === "RU") {
      return (
        <Marker coordinates={[country.latLng?.capital[1], country.latLng?.capital[0]]}>
          <text textAnchor="middle" fontSize={7} style={{ cursor: "pointer"}}>{country.name}</text>
        </Marker>
      )
    }

    return (
      <Marker coordinates={[country.latLng?.country[1], country.latLng?.country[0]]}>
        <text textAnchor="middle" fontSize={7} style={{ cursor: "pointer"}}>{country.name}</text>
      </Marker>
    )
  }

  const handleZoom = ({ coordinates, zoom } : { coordinates: any, zoom: number }) => {
    console.log("zoom", zoom);
  }

  return (
    <div className="w-full h-screen overflow-hidden bg-green-50">
      <ComposableMap
        projection="geoAzimuthalEqualArea"
        projectionConfig={{ scale: 820, rotate: [-15, -55, 0], center: [0, -2.5] }}
        style={{ width: "100%", height: "100%" }}
        preserveAspectRatio="xMidYMid meet"
      >
        <ZoomableGroup
          zoom={1}
          onMoveStart={({ coordinates, zoom }) => handleZoom({ coordinates, zoom })}
        >
          <>
          <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => renderGeography(geo))
          }
        </Geographies>
        
        {countries.map((country: Country) => renderCountryNameMarker(country))}
        </>
      </ZoomableGroup>
      </ComposableMap>
    </div>
  )
}

export default App
