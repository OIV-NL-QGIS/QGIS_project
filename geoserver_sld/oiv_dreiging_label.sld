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
          <Name>Dreiging</Name>
          <Title>Dreiging</Title>
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
        <!-- Aanrijding -->
        <Rule>
          <Name>Aanrijding</Name>
          <Title>Aanrijding</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg001_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Accus en klein chemisch materiaal -->
        <Rule>
          <Name>Accus en klein chemisch materiaal</Name>
          <Title>Accus en klein chemisch materiaal</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg002_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Agressie -->
        <Rule>
          <Name>Agressie</Name>
          <Title>Agressie</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg003_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Algemeen gevaar -->
        <Rule>
          <Name>Algemeen gevaar</Name>
          <Title>Algemeen gevaar</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg004_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Asbest -->
        <Rule>
          <Name>Asbest</Name>
          <Title>Asbest</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg005_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Beknelling -->
        <Rule>
          <Name>Beknelling</Name>
          <Title>Beknelling</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg006_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Beschadiging -->
        <Rule>
          <Name>Beschadiging</Name>
          <Title>Beschadiging</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg007_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Besmetting -->
        <Rule>
          <Name>Besmetting</Name>
          <Title>Besmetting</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg008_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Bijtende stoffen -->
        <Rule>
          <Name>Bijtende stoffen</Name>
          <Title>Bijtende stoffen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg009_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Bijtgevaar -->
        <Rule>
          <Name>Bijtgevaar</Name>
          <Title>Bijtgevaar</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg010_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Biologische agentia-infectueus -->
        <Rule>
          <Name>Biologische agentia-infectueus</Name>
          <Title>Biologische agentia-infectueus</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg011_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Brandgevaarlijk -->
        <Rule>
          <Name>Brandgevaarlijk</Name>
          <Title>Brandgevaarlijk</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg012_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Desorientatie -->
        <Rule>
          <Name>Desorientatie</Name>
          <Title>Desorientatie</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg013_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Drukgolf -->
        <Rule>
          <Name>Drukgolf</Name>
          <Title>Drukgolf</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg014_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Elektrische spanning -->
        <Rule>
          <Name>Elektrische spanning</Name>
          <Title>Elektrische spanning</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg015_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Elektrisering -->
        <Rule>
          <Name>Elektrisering</Name>
          <Title>Elektrisering</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg016_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Exotische dieren -->
        <Rule>
          <Name>Exotische dieren</Name>
          <Title>Exotische dieren</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg017_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Explosie -->
        <Rule>
          <Name>Explosie</Name>
          <Title>Explosie</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg018_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Explosieve atmosfeer -->
        <Rule>
          <Name>Explosieve atmosfeer</Name>
          <Title>Explosieve atmosfeer</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg019_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Explosieve stoffen -->
        <Rule>
          <Name>Explosieve stoffen</Name>
          <Title>Explosieve stoffen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg020_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Gastank -->
        <Rule>
          <Name>Gastank</Name>
          <Title>Gastank</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg021_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS XX -->
        <Rule>
          <Name>GHS XX</Name>
          <Title>GHS XX</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg022_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS01 Explosief -->
        <Rule>
          <Name>GHS01 Explosief</Name>
          <Title>GHS01 Explosief</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg023_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS02 Ontvlambaar -->
        <Rule>
          <Name>GHS02 Ontvlambaar</Name>
          <Title>GHS02 Ontvlambaar</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg024_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS03 Brand bevorderend (oxiderend) -->
        <Rule>
          <Name>GHS03 Brand bevorderend (oxiderend)</Name>
          <Title>GHS03 Brand bevorderend (oxiderend)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg025_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS04 Houder onder druk -->
        <Rule>
          <Name>GHS04 Houder onder druk</Name>
          <Title>GHS04 Houder onder druk</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg026_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS05 Corrosief (Bijtend) -->
        <Rule>
          <Name>GHS05 Corrosief (Bijtend)</Name>
          <Title>GHS05 Corrosief (Bijtend)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg027_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS06 Giftig -->
        <Rule>
          <Name>GHS06 Giftig</Name>
          <Title>GHS06 Giftig</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg028_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS07 Schadelijk Irriterend allergische huidreactie -->
        <Rule>
          <Name>GHS07 Schadelijk Irriterend allergische huidreactie</Name>
          <Title>GHS07 Schadelijk Irriterend allergische huidreactie</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg029_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS08 Gezondheidsgevaar op lange termijn -->
        <Rule>
          <Name>GHS08 Gezondheidsgevaar op lange termijn</Name>
          <Title>GHS08 Gezondheidsgevaar op lange termijn</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg030_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- GHS09 Milieugevaarlijk -->
        <Rule>
          <Name>GHS09 Milieugevaarlijk</Name>
          <Title>GHS09 Milieugevaarlijk</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg031_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Giftige stoffen -->
        <Rule>
          <Name>Giftige stoffen</Name>
          <Title>Giftige stoffen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg032_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Glad oppervlak -->
        <Rule>
          <Name>Glad oppervlak</Name>
          <Title>Glad oppervlak</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg033_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Hangende lasten -->
        <Rule>
          <Name>Hangende lasten</Name>
          <Title>Hangende lasten</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg034_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Heet oppervlak -->
        <Rule>
          <Name>Heet oppervlak</Name>
          <Title>Heet oppervlak</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg035_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Helling -->
        <Rule>
          <Name>Helling</Name>
          <Title>Helling</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg036_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Honden bewaking -->
        <Rule>
          <Name>Honden bewaking</Name>
          <Title>Honden bewaking</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg037_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Houder onder druk -->
        <Rule>
          <Name>Houder onder druk</Name>
          <Title>Houder onder druk</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg038_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Implosie -->
        <Rule>
          <Name>Implosie</Name>
          <Title>Implosie</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg039_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Insluiting -->
        <Rule>
          <Name>Insluiting</Name>
          <Title>Insluiting</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg040_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Instorting -->
        <Rule>
          <Name>Instorting</Name>
          <Title>Instorting</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg041_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Kortsluiting -->
        <Rule>
          <Name>Kortsluiting</Name>
          <Title>Kortsluiting</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg042_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Laadpaal EV -->
        <Rule>
          <Name>Laadpaal EV</Name>
          <Title>Laadpaal EV</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg043_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Lage temperatuur-bevriezing -->
        <Rule>
          <Name>Lage temperatuur-bevriezing</Name>
          <Title>Lage temperatuur-bevriezing</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg044_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Langetermijn gezondheidsschade -->
        <Rule>
          <Name>Langetermijn gezondheidsschade</Name>
          <Title>Langetermijn gezondheidsschade</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg045_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Laserstralen -->
        <Rule>
          <Name>Laserstralen</Name>
          <Title>Laserstralen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg046_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Li-ion batterijen -->
        <Rule>
          <Name>Li-ion batterijen</Name>
          <Title>Li-ion batterijen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg047_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Magnetisch veld -->
        <Rule>
          <Name>Magnetisch veld</Name>
          <Title>Magnetisch veld</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg048_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Niet met water blussen -->
        <Rule>
          <Name>Niet met water blussen</Name>
          <Title>Niet met water blussen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg049_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Niet-ioniserende straling -->
        <Rule>
          <Name>Niet-ioniserende straling</Name>
          <Title>Niet-ioniserende straling</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg050_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Op afstand bestuurde machines -->
        <Rule>
          <Name>Op afstand bestuurde machines</Name>
          <Title>Op afstand bestuurde machines</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg051_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Oxiderende stoffen -->
        <Rule>
          <Name>Oxiderende stoffen</Name>
          <Title>Oxiderende stoffen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg052_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Radioactief materiaal -->
        <Rule>
          <Name>Radioactief materiaal</Name>
          <Title>Radioactief materiaal</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg053_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Schadelijk voor het milieu -->
        <Rule>
          <Name>Schadelijk voor het milieu</Name>
          <Title>Schadelijk voor het milieu</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg054_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Straling -->
        <Rule>
          <Name>Straling</Name>
          <Title>Straling</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg055_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Stroming -->
        <Rule>
          <Name>Stroming</Name>
          <Title>Stroming</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg056_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Valgevaar -->
        <Rule>
          <Name>Valgevaar</Name>
          <Title>Valgevaar</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg057_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Verdrinking -->
        <Rule>
          <Name>Verdrinking</Name>
          <Title>Verdrinking</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg058_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Verstikking -->
        <Rule>
          <Name>Verstikking</Name>
          <Title>Verstikking</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg059_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Verwonding -->
        <Rule>
          <Name>Verwonding</Name>
          <Title>Verwonding</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg060_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Zonnepanelen -->
        <Rule>
          <Name>Zonnepanelen</Name>
          <Title>Zonnepanelen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/drg061_a.svg"/>
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
