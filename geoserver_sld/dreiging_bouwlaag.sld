<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" version="1.1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
  <NamedLayer>
    <se:Name>Dreiging bouwlaag</se:Name>
    <UserStyle>
      <se:Name>Dreiging bouwlaag</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>Biologische agentia</se:Name>
          <se:Description>
            <se:Title>Biologische agentia</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>101</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/biologische_agentia.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>                
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Bijtende stoffen</se:Name>
          <se:Description>
            <se:Title>Bijtende stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>102</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/bijtende_stoffen.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Oxiderende stoffen</se:Name>
          <se:Description>
            <se:Title>Oxiderende stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>103</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/oxiderende_stoffen.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Niet blussen met water</se:Name>
          <se:Description>
            <se:Title>Niet blussen met water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>104</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/niet_blussen_met_water.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Ontvlambare stoffen</se:Name>
          <se:Description>
            <se:Title>Ontvlambare stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>105</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/ontvlambare_stoffen.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Giftige stoffen</se:Name>
          <se:Description>
            <se:Title>Giftige stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>106</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/giftige_stoffen.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Explosieve stoffen</se:Name>
          <se:Description>
            <se:Title>Explosieve stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>107</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/explosieve_stoffen.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Electrische spanning</se:Name>
          <se:Description>
            <se:Title>Electrische spanning</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>108</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/electrische_spanning.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Magnetisch veld</se:Name>
          <se:Description>
            <se:Title>Magnetisch veld</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>109</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/magnetisch_veld.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Niet-ioniserende straling</se:Name>
          <se:Description>
            <se:Title>Niet-ioniserende straling</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>110</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/niet_ioniserende_straling.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Radioactief materiaal</se:Name>
          <se:Description>
            <se:Title>Radioactief materiaal</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>111</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/radioactief_materiaal.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Lage temperatuur of bevriezing</se:Name>
          <se:Description>
            <se:Title>Lage temperatuur of bevriezing</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>112</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/lage_temperatuur.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Asbest</se:Name>
          <se:Description>
            <se:Title>Asbest</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>113</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/asbest.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Laserstralen</se:Name>
          <se:Description>
            <se:Title>Laserstralen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>114</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/laserstralen.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Ontvlambare stoffen</se:Name>
          <se:Description>
            <se:Title>Ontvlambare stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>201</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/ontvlambare_stoffen_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Oxiderende stoffen</se:Name>
          <se:Description>
            <se:Title>Oxiderende stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>202</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/oxiderende_stoffen_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Ontplofbare stoffen</se:Name>
          <se:Description>
            <se:Title>Ontplofbare stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>203</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/ontplofbare_stoffen_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Corrosieve stoffen</se:Name>
          <se:Description>
            <se:Title>Corrosieve stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>204</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/corrosieve_stoffen_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Giftige stoffen</se:Name>
          <se:Description>
            <se:Title>Giftige stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>205</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/giftige_stoffen_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Accuut gevaar</se:Name>
          <se:Description>
            <se:Title>Accuut gevaar</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>206</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/accuut_gevaar_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Gassen onder druk</se:Name>
          <se:Description>
            <se:Title>Gassen onder druk</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>207</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/gassen_onder_druk_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Gevaar aquatisch milieu</se:Name>
          <se:Description>
            <se:Title>Gevaar aquatisch milieu</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>208</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/gevaar_aquatisch_milieu_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Gevaar gezondheid</se:Name>
          <se:Description>
            <se:Title>Gevaar gezondheid</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>209</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
               <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/gevaar_gezondheid_ghs.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Val gevaar</se:Name>
          <se:Description>
            <se:Title>Val gevaar</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>115</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/val_gevaar.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Bijt gevaar</se:Name>
          <se:Description>
            <se:Title>Bijt gevaar</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>116</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/bijt_gevaar.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Klein chemisch</se:Name>
          <se:Description>
            <se:Title>Klein chemisch</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>117</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/klein_chemisch.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Explosieve atmosfeer</se:Name>
          <se:Description>
            <se:Title>Explosieve atmosfeer</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>118</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/explosieve_atmosfeer.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Lithiumhoudende batterijen</se:Name>
          <se:Description>
            <se:Title>Lithiumhoudende batterijen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>119</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/lithiumhoudende_batterijen.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Exotische dieren</se:Name>
          <se:Description>
            <se:Title>Exotische dieren</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>120</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/exotische_dieren.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Schadelijk voor milieu</se:Name>
          <se:Description>
            <se:Title>Schadelijk voor milieu</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>121</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/schadelijk_voor_milieu.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Glad oppervlak</se:Name>
          <se:Description>
            <se:Title>Glad oppervlak</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>122</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/glad_oppervlak.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Hangende lasten</se:Name>
          <se:Description>
            <se:Title>Hangende lasten</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>123</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/hangende_lasten.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Heet oppervlak</se:Name>
          <se:Description>
            <se:Title>Heet oppervlak</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>124</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/heet_oppervlak.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Houder onder druk</se:Name>
          <se:Description>
            <se:Title>Houder onder druk</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>125</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/houder_onder_druk.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Op afstand bestuurde machines</se:Name>
          <se:Description>
            <se:Title>Op afstand bestuurde machines</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>126</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/op_afstand_bestuurde_machines.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Helling</se:Name>
          <se:Description>
            <se:Title>Helling</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>127</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/helling.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Langetermijn gezondheidsschade</se:Name>
          <se:Description>
            <se:Title>Langetermijn gezondheidsschade</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>dreiging_type_id</ogc:PropertyName>
              <ogc:Literal>128</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:href="./oiv/langetermijn_gezondheidsschade.png" xlink:type="simple"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
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
              <se:SvgParameter name="font-size">1.4</se:SvgParameter>
            </se:Font>
            <se:LabelPlacement>
              <se:PointPlacement>
                <se:AnchorPoint>
                  <se:AnchorPointX>0.5</se:AnchorPointX>
                  <se:AnchorPointY>0.5</se:AnchorPointY>
                </se:AnchorPoint>
                <se:Displacement>
                  <se:DisplacementX>0</se:DisplacementX>
                  <se:DisplacementY>-10</se:DisplacementY>
                </se:Displacement>                
                <Rotation>
                  <ogc:PropertyName>rotatie</ogc:PropertyName>
                </Rotation>
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
