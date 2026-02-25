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
          <Name>Alternatief bluswater</Name>
          <Title>Alternatief bluswater</Title>
          <MaxScaleDenominator>5000</MaxScaleDenominator>
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
           LEGENDA ONLY RULES
           =============================== -->
        <!-- Afsluiter omloop -->
        <Rule>
          <Name>Afsluiter omloop</Name>
          <Title>Afsluiter omloop</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/vvz009_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Blusleiding afnamepunt -->
        <Rule>
          <Name>Blusleiding afnamepunt</Name>
          <Title>Blusleiding afnamepunt</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/vvz030_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Blusleiding vulpunt -->
        <Rule>
          <Name>Blusleiding vulpunt</Name>
          <Title>Blusleiding vulpunt</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/vvz035_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Bluswaterriool -->
        <Rule>
          <Name>Bluswaterriool</Name>
          <Title>Bluswaterriool</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn001_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Bluswaterriool (particulier) -->
        <Rule>
          <Name>Bluswaterriool (particulier)</Name>
          <Title>Bluswaterriool (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn011_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Bovengrondse brandkraan -->
        <Rule>
          <Name>Bovengrondse brandkraan</Name>
          <Title>Bovengrondse brandkraan</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn002_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Bovengrondse brandkraan (particulier) -->
        <Rule>
          <Name>Bovengrondse brandkraan (particulier)</Name>
          <Title>Bovengrondse brandkraan (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn012_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Geboorde putten - dicht -->
        <Rule>
          <Name>Geboorde putten - dicht</Name>
          <Title>Geboorde putten - dicht</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn003_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Geboorde putten - dicht (particulier) -->
        <Rule>
          <Name>Geboorde putten - dicht (particulier)</Name>
          <Title>Geboorde putten - dicht (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn013_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Geboorde putten - open -->
        <Rule>
          <Name>Geboorde putten - open</Name>
          <Title>Geboorde putten - open</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn004_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Geboorde putten - open (particulier) -->
        <Rule>
          <Name>Geboorde putten - open (particulier)</Name>
          <Title>Geboorde putten - open (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn014_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Ondergrondse brandkraan (particulier) -->
        <Rule>
          <Name>Ondergrondse brandkraan (particulier)</Name>
          <Title>Ondergrondse brandkraan (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn015_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Open water -->
        <Rule>
          <Name>Open water</Name>
          <Title>Open water</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn007_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Open water (particulier) -->
        <Rule>
          <Name>Open water (particulier)</Name>
          <Title>Open water (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn017_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Open water xxx zijde -->
        <Rule>
          <Name>Open water xxx zijde</Name>
          <Title>Open water xxx zijde</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn006_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Open water xxx zijde (particulier) -->
        <Rule>
          <Name>Open water xxx zijde (particulier)</Name>
          <Title>Open water xxx zijde (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn016_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Opstelplaats WTS -->
        <Rule>
          <Name>Opstelplaats WTS</Name>
          <Title>Opstelplaats WTS</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/osp009_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Opvoerpomp of bronpomp -->
        <Rule>
          <Name>Opvoerpomp of bronpomp</Name>
          <Title>Opvoerpomp of bronpomp</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn008_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Opvoerpomp of bronpomp (particulier) -->
        <Rule>
          <Name>Opvoerpomp of bronpomp (particulier)</Name>
          <Title>Opvoerpomp of bronpomp (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn018_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Water innamepunt (WIP) -->
        <Rule>
          <Name>Water innamepunt (WIP)</Name>
          <Title>Water innamepunt (WIP)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn009_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Water innamepunt (WIP) (particulier) -->
        <Rule>
          <Name>Water innamepunt (WIP) (particulier)</Name>
          <Title>Water innamepunt (WIP) (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn019_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Waterkelder - buffer -->
        <Rule>
          <Name>Waterkelder - buffer</Name>
          <Title>Waterkelder - buffer</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn010_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Waterkelder - buffer (particulier) -->
        <Rule>
          <Name>Waterkelder - buffer (particulier)</Name>
          <Title>Waterkelder - buffer (particulier)</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/wwn020_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Niet bruikbaar -->
        <Rule>
          <Name>Niet bruikbaar</Name>
          <Title>Niet bruikbaar</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/vvz046_c.svg"/>
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
