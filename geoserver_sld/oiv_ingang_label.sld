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
          <Name>Ingang</Name>
          <Title>Ingang</Title>
          <PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
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
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
          </PointSymbolizer>
        <!-- ===============================
             CENTRALE TEXT SYMBOLIZER
             =============================== -->
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label>
              <ogc:PropertyName>label</ogc:PropertyName>
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
        <!-- Brandweeringang -->
        <Rule>
          <Name>Brandweeringang</Name>
          <Title>Brandweeringang</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn001_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Brandweerlift -->
        <Rule>
          <Name>Brandweerlift</Name>
          <Title>Brandweerlift</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn002_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Deur L -->
        <Rule>
          <Name>Deur L</Name>
          <Title>Deur L</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn003_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Deur R -->
        <Rule>
          <Name>Deur R</Name>
          <Title>Deur R</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn004_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Generieke trap -->
        <Rule>
          <Name>Generieke trap</Name>
          <Title>Generieke trap</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn005_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Ingang gebied terrein -->
        <Rule>
          <Name>Ingang gebied terrein</Name>
          <Title>Ingang gebied terrein</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn006_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Lift -->
        <Rule>
          <Name>Lift</Name>
          <Title>Lift</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn007_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Neveningang -->
        <Rule>
          <Name>Neveningang</Name>
          <Title>Neveningang</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn009_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Neveningang  gebied terrein -->
        <Rule>
          <Name>Neveningang  gebied terrein</Name>
          <Title>Neveningang  gebied terrein</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn008_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Nooduitgang -->
        <Rule>
          <Name>Nooduitgang</Name>
          <Title>Nooduitgang</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/vvz049_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Schuifdeur dubbel -->
        <Rule>
          <Name>Schuifdeur dubbel</Name>
          <Title>Schuifdeur dubbel</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn010_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Schuifdeur enkel links -->
        <Rule>
          <Name>Schuifdeur enkel links</Name>
          <Title>Schuifdeur enkel links</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn011_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Schuifdeur enkel rechts -->
        <Rule>
          <Name>Schuifdeur enkel rechts</Name>
          <Title>Schuifdeur enkel rechts</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn012_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- SOS toegang -->
        <Rule>
          <Name>SOS toegang</Name>
          <Title>SOS toegang</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn015_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Trap bordes -->
        <Rule>
          <Name>Trap bordes</Name>
          <Title>Trap bordes</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn016_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Trap recht -->
        <Rule>
          <Name>Trap recht</Name>
          <Title>Trap recht</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn017_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Trap rond -->
        <Rule>
          <Name>Trap rond</Name>
          <Title>Trap rond</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/tgn018_a.svg"/>
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
