export async function getCountries() {
  return await fetch("http://127.0.0.1:8000/api/v1/countries")
    .then(response => response.json())
}