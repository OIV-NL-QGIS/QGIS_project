<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0"
  xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
  xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <NamedLayer>
    <Name></Name>
    <UserStyle>
      <Name>Pie charts</Name>
      <FeatureTypeStyle>
        <Rule>
          <PointSymbolizer>
          <Geometry>
          <ogc:Function name="centroid">
            <ogc:PropertyName>geom</ogc:PropertyName>
          </ogc:Function>
        </Geometry>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:type="simple"
                  xlink:href="http://chart.apis.google.com/chart?cht=p3&amp;chs=350x250&amp;chdl=${up_to_date}|${binnen_3_maanden}|${updaten}|${nog_maken}&amp;chdlp=b|0,1,2,3&amp;chco=00ff00|ff8300|ff0000|0000ff&amp;chp=0&amp;chf=bg,s,FFFFFF00&amp;chdls=000000,48&amp;chd=t:${up_to_date},${binnen_3_maanden},${updaten},${nog_maken}"/>
                <Format>image/png</Format>
              </ExternalGraphic>
              <Size>75</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
