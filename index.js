var baseurl = "https://incomehealth.herokuapp.com/api/v1.0";
var healthcare = "/US_healthcare_cost";
var food = "/fooddata/";
var countrynames = "/countrynames";
var metrics = "/foodindex";
var starting_country = "USA, Puerto Rico and US Virgin Islands";



// This function is called when a dropdown menu item is selected
d3.json(baseurl + food + starting_country, function(data) {
    console.log(data);
});












