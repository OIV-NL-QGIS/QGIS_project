<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:se="http://www.opengis.net/se">
  <NamedLayer>
    <se:Name>Update van objecten</se:Name>
    <UserStyle>
      <se:Name>Update van objecten</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>nog niet gemaakt</se:Name>
          <se:Description>
            <se:Title>nog niet gemaakt</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>conditie</ogc:PropertyName>
              <ogc:Literal>nog niet gemaakt</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PointSymbolizer>
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/info.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>25</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>up-to-date</se:Name>
          <se:Description>
            <se:Title>up-to-date</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>conditie</ogc:PropertyName>
              <ogc:Literal>up-to-date</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PointSymbolizer>
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/info_groen.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>25</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>updaten binnen 3 maanden</se:Name>
          <se:Description>
            <se:Title>updaten binnen 3 maanden</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>conditie</ogc:PropertyName>
              <ogc:Literal>updaten binnen 3 maanden</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PointSymbolizer>
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/info_oranje.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>25</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>updaten</se:Name>
          <se:Description>
            <se:Title>updaten</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>conditie</ogc:PropertyName>
              <ogc:Literal>updaten</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PointSymbolizer>
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/info_rood.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>25</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
