<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:ogc="http://www.opengis.net/ogc" xmlns:se="http://www.opengis.net/se" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0">
  <NamedLayer>
    <se:Name>Ingang bouwlaag</se:Name>
    <UserStyle>
      <se:Name>Ingang bouwlaag</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>Brandweeringang</se:Name>
          <se:Description>
            <se:Title>Brandweeringang</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>ingang_type_id</ogc:PropertyName>
              <ogc:Literal>32</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/brandweeringang.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>10</se:Size>
            <se:Rotation>
            <ogc:PropertyName>rotatie</ogc:PropertyName>
          </se:Rotation>              
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Neveningang</se:Name>
          <se:Description>
            <se:Title>Neveningang</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>ingang_type_id</ogc:PropertyName>
              <ogc:Literal>47</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/neveningang.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>10</se:Size>
              <se:Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </se:Rotation>              
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Brandweerlift</se:Name>
          <se:Description>
            <se:Title>Brandweerlift</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>ingang_type_id</ogc:PropertyName>
              <ogc:Literal>35</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/brandweerlift.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>4</se:Size>
              <se:Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </se:Rotation> 
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Lift</se:Name>
          <se:Description>
            <se:Title>Lift</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>ingang_type_id</ogc:PropertyName>
              <ogc:Literal>165</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/lift.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>4</se:Size>
              <se:Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </se:Rotation> 
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Trap rond</se:Name>
          <se:Description>
            <se:Title>Trap rond</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>ingang_type_id</ogc:PropertyName>
              <ogc:Literal>173</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/trap_rond.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>7</se:Size>
              <se:Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </se:Rotation> 
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Trap recht</se:Name>
          <se:Description>
            <se:Title>Trap recht</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>ingang_type_id</ogc:PropertyName>
              <ogc:Literal>174</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/trap_recht.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>7</se:Size>
              <se:Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </se:Rotation> 
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Trap bordes</se:Name>
          <se:Description>
            <se:Title>Trap bordes</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>ingang_type_id</ogc:PropertyName>
              <ogc:Literal>153</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/trap_bordes.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>7</se:Size>
              <se:Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </se:Rotation> 
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Nooduitgang</se:Name>
          <se:Description>
            <se:Title>Nooduitgang</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>ingang_type_id</ogc:PropertyName>
              <ogc:Literal>1011</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/nooduitgang.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <se:Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </se:Rotation> 
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Label>
              <ogc:PropertyName>label</ogc:PropertyName>
            </se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">MS Shell Dlg 2</se:SvgParameter>
              <se:SvgParameter name="font-size">2</se:SvgParameter>
            </se:Font>
            <se:LabelPlacement>
              <se:PointPlacement>
                <se:AnchorPoint>
                  <se:AnchorPointX>0.5</se:AnchorPointX>
                  <se:AnchorPointY>0.5</se:AnchorPointY>
                </se:AnchorPoint>
              </se:PointPlacement>
            </se:LabelPlacement>
            <se:Halo>
              <se:Radius>0.10000000000000001</se:Radius>
              <se:Fill>
                <se:SvgParameter name="fill">#ffffff</se:SvgParameter>
              </se:Fill>
            </se:Halo>
            <se:Fill>
              <se:SvgParameter name="fill">#000000</se:SvgParameter>
            </se:Fill>
          </se:TextSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
