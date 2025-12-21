<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0"
    xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
    xmlns="http://www.opengis.net/sld"
    xmlns:ogc="http://www.opengis.net/ogc"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <NamedLayer>
    <Name>POI_Symbols</Name>
    <UserStyle>
      <Title>POI Dynamic Symbols</Title>

      <FeatureTypeStyle>

        <!-- ===============================
             DYNAMISCHE SYMBOLIZER
             =============================== -->
        <Rule>
          <Name>Repressief object</Name>
          <Title>Repressief object</Title>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/${symbol_name}.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/png/${symbol_name}.png"/>
                <Format>image/png</Format>
              </ExternalGraphic>
              <Size>
                <ogc:Mul>
                  <ogc:PropertyName>size</ogc:PropertyName>
                  <ogc:Literal>1</ogc:Literal>
                </ogc:Mul>
              </Size>
            </Graphic>
          </PointSymbolizer>
        <!-- ===============================
             CENTRALE TEXT SYMBOLIZER
             =============================== -->
          <TextSymbolizer>
            <Label>
              <ogc:PropertyName>formelenaam</ogc:PropertyName>
            </Label>
            <Font>
              <CssParameter name="font-size">
                <ogc:Mul>
                  <ogc:PropertyName>size</ogc:PropertyName>
                  <ogc:Literal>0.25</ogc:Literal>
                </ogc:Mul>
              </CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX><ogc:PropertyName>anch_x</ogc:PropertyName></AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
                <Displacement>
                  <DisplacementX>
                    <ogc:Mul>
                      <ogc:Mul>
                        <ogc:PropertyName>size</ogc:PropertyName>
                        <ogc:PropertyName>dx_factor</ogc:PropertyName>
                      </ogc:Mul>
                      <ogc:Literal>0.8</ogc:Literal>
                    </ogc:Mul>
                  </DisplacementX>
                  <DisplacementY>
                    <ogc:Mul>
                      <ogc:Mul>
                        <ogc:PropertyName>size</ogc:PropertyName>
                        <ogc:PropertyName>dy_factor</ogc:PropertyName>
                      </ogc:Mul>
                      <ogc:Literal>1</ogc:Literal>
                    </ogc:Mul>
                  </DisplacementY>
                </Displacement>
              </PointPlacement>
            </LabelPlacement>
            <Halo>
              <Radius>0.1</Radius>
              <Fill>
                <CssParameter name="fill">#ffffff</CssParameter>
              </Fill>
            </Halo>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill>
            <VendorOption name="conflictResolution">false</VendorOption>
          </TextSymbolizer>
        </Rule>

      </FeatureTypeStyle>
      <FeatureTypeStyle>
      <!-- ===============================
           LEGENDA ONLY RULES (alle 43 POI)
           =============================== -->
        <!-- Evenement A -->
        <Rule>
          <Name>Evenement A</Name>
          <Title>Evenement A</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/ter001_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Evenement B -->
        <Rule>
          <Name>Evenement B</Name>
          <Title>Evenement B</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/ter002_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Evenement C -->
        <Rule>
          <Name>Evenement C</Name>
          <Title>Evenement C</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/ter003_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Gebouw -->
        <Rule>
          <Name>Gebouw</Name>
          <Title>Gebouw</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/ter004_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Infrastructuur -->
        <Rule>
          <Name>Infrastructuur</Name>
          <Title>Infrastructuur</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/ter005_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Natuur -->
        <Rule>
          <Name>Natuur</Name>
          <Title>Natuur</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/ter006_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Water -->
        <Rule>
          <Name>Water</Name>
          <Title>Water</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/ter007_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
