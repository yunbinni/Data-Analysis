library('tidyverse')
library('leaflet')

leaflet() %>%
    setView(lng=126.9784, lat=37.566, zoom=11) %>%
    addTiles()

st <- read.csv('주유소.csv') %>% as_tibble
st

leaflet(st) %>%
    setView(lng=126.9784, lat=37.566, zoom=11) %>%
    addProviderTiles('CartoDB.Positron') %>%
    addCircles(lng=~경도, lat=~위도, color='#006633') %>% 
    addMarkers(lng=~경도, lat=~위도,
           clusterOptions = markerClusterOptions(),
           popup = st$'상호명')

