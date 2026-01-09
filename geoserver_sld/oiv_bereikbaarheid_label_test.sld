<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" version="1.1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
  <NamedLayer>
    <se:Name>Bereikbaarheid</se:Name>
    <UserStyle>
      <se:Name>Bereikbaarheid</se:Name>
      
      <!-- Lijnen bottom -->
      <se:FeatureTypeStyle>
        <!-- Solid -->
        <se:Rule>
          <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Stroke>
              <se:SvgParameter name="stroke">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/0/lijnkleur</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-width">
                <ogc:Mul>
                  <ogc:Function name="jsonPointer">
                    <ogc:PropertyName>styles</ogc:PropertyName>
                    <ogc:Literal>/style/0/lijndikte</ogc:Literal>
                  </ogc:Function>
                  <ogc:Literal>2</ogc:Literal>
                </ogc:Mul>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/0/verbindingsstijl</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-linecap">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/0/eindstijl</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-opacity">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/0/lijnopacity</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
            </se:Stroke>
          </se:LineSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>

      <!-- Lijnen middle -->
      <se:FeatureTypeStyle>
        <!-- Solid -->
        <se:Rule>
          <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Stroke>
              <se:SvgParameter name="stroke">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/1/lijnkleur</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-width">
                <ogc:Mul>
                  <ogc:Function name="jsonPointer">
                    <ogc:PropertyName>styles</ogc:PropertyName>
                    <ogc:Literal>/style/1/lijndikte</ogc:Literal>
                  </ogc:Function>
                  <ogc:Literal>2</ogc:Literal>
                </ogc:Mul>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/1/verbindingsstijl</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-linecap">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/1/eindstijl</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-opacity">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/1/lijnopacity</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
            </se:Stroke>
          </se:LineSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>


      <!-- Symbolen op lijn -->
      <se:FeatureTypeStyle>
        <!-- Aanrijdroute - Legenda en driehoek -->
        <se:Rule>
          <se:Name>Aanrijdroute</se:Name>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>soort</ogc:PropertyName>
              <ogc:Literal>aanrijdroute</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Stroke>
              <se:SvgParameter name="stroke">#00ae22</se:SvgParameter>
              <se:SvgParameter name="stroke-width">
                <ogc:Mul>
                  <ogc:Function name="jsonPointer">
                    <ogc:PropertyName>styles</ogc:PropertyName>
                    <ogc:Literal>/style/1/lijndikte</ogc:Literal>
                  </ogc:Function>
                  <ogc:Literal>2</ogc:Literal>
                </ogc:Mul>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/1/verbindingsstijl</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-linecap">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/1/eindstijl</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
              <se:SvgParameter name="stroke-opacity">
                <ogc:Function name="jsonPointer">
                  <ogc:PropertyName>styles</ogc:PropertyName>
                  <ogc:Literal>/style/1/lijnopacity</ogc:Literal>
                </ogc:Function>
              </se:SvgParameter>
            </se:Stroke>
          </se:LineSymbolizer>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
			      <se:Geometry>
              <ogc:Function name="endPoint">
                <ogc:PropertyName>geom</ogc:PropertyName>
              </ogc:Function>
            </se:Geometry>
            <se:Graphic>
              <se:Mark>
                <se:WellKnownName>triangle</se:WellKnownName>
                <se:Fill>
                  <se:SvgParameter name="fill">#00ae22</se:SvgParameter>
                </se:Fill>
              </se:Mark>
              <se:Size>
                <ogc:Mul>
                  <ogc:Function name="jsonPointer">
                    <ogc:PropertyName>styles</ogc:PropertyName>
                    <ogc:Literal>/style/0/lijndikte</ogc:Literal>
                  </ogc:Function>
                  <ogc:Literal>8</ogc:Literal>
                </ogc:Mul>
              </se:Size>
              <se:Rotation>
                <ogc:Add> 
                  <ogc:Function name="endAngle"> 
                    <ogc:PropertyName>geom</ogc:PropertyName> 
                  </ogc:Function> 
                  <ogc:Literal>90.0</ogc:Literal> 
                </ogc:Add> 
              </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>

        <!-- Hekwerk en Afrastering - kruis -->
        <se:Rule>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Or>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>soort</ogc:PropertyName>
                <ogc:Literal>hekwerk</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsLike wildCard="%" singleChar="_" escapeChar="\">
                <ogc:PropertyName>soort</ogc:PropertyName>
                <ogc:Literal>Afrastering%</ogc:Literal>
              </ogc:PropertyIsLike>
            </ogc:Or>
          </ogc:Filter>
          <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Stroke>
              <se:GraphicStroke>
                <se:Graphic>
                  <se:Mark>
                    <se:WellKnownName>shape://times</se:WellKnownName>
                    <se:Stroke>
                      <se:SvgParameter name="stroke">                
                        <ogc:Function name="jsonPointer">
                          <ogc:PropertyName>styles</ogc:PropertyName>
                          <ogc:Literal>/style/0/lijnkleur</ogc:Literal>
                        </ogc:Function>
                      </se:SvgParameter>
                      <se:SvgParameter name="stroke-width">
                        <ogc:Mul>
                          <ogc:Function name="jsonPointer">
                            <ogc:PropertyName>styles</ogc:PropertyName>
                            <ogc:Literal>/style/0/lijndikte</ogc:Literal>
                          </ogc:Function>
                          <ogc:Literal>2</ogc:Literal>
                        </ogc:Mul>
                      </se:SvgParameter>
                    </se:Stroke>
                  </se:Mark>
                  <se:Size>
                    <ogc:Mul>
                      <ogc:Function name="jsonPointer">
                        <ogc:PropertyName>styles</ogc:PropertyName>
                        <ogc:Literal>/style/1/lijndikte</ogc:Literal>
                      </ogc:Function>
                      <ogc:Literal>1</ogc:Literal>
                    </ogc:Mul>
                  </se:Size>
                </se:Graphic>
              </se:GraphicStroke>
              <se:SvgParameter name="stroke-dasharray">2 2</se:SvgParameter>
            </se:Stroke>
          </se:LineSymbolizer>
        </se:Rule> 
      </se:FeatureTypeStyle>

    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
