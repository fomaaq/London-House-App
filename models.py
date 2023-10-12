from dataclasses import dataclass


@dataclass
class House():
    index: int
    id: int
    bedrooms: int
    bathrooms: int
    tenure: str
    garden: int
    street: str
    size_sqft: int
    price_pounds: int
    nearest_station_name: str
    nearest_station_miles: float
    postcode_outer: str

    def from_data(item: tuple):
        return House(
            index=item[0],
            id=item[1],
            bedrooms=item[2],
            bathrooms=item[3],
            tenure=item[4],
            garden=item[5],
            street=item[6],
            size_sqft=item[7],
            price_pounds=item[8],
            nearest_station_name=item[9],
            nearest_station_miles=item[10],
            postcode_outer=item[11],
        )
