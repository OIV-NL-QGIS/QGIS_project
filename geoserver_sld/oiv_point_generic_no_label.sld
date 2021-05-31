<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0"
  xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
  xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <NamedLayer>
    <Name>Symbol</Name>
    <UserStyle>
      <Title>Symbol</Title>
      <FeatureTypeStyle>
        <Rule>
          <Title>Symbol</Title>
          <MinScaleDenominator>1</MinScaleDenominator>
          <MaxScaleDenominator>2500</MaxScaleDenominator>               
          <PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="./png/${symbol_name}.png"/>
                <Format>image/png</Format>
              </ExternalGraphic>
              <Size>
              	<ogc:Mul>
                  <ogc:PropertyName>size</ogc:PropertyName>
                  <ogc:Literal>2.5</ogc:Literal>
                </ogc:Mul>
              </Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
          </PointSymbolizer>        
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
