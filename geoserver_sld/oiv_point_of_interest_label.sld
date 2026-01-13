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
          <Name>Points of interest</Name>
          <Title>Points of interest</Title>
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
        <!-- Afsluitpaal of poller -->
        <Rule>
          <Name>Afsluitpaal of poller</Name>
          <Title>Afsluitpaal of poller</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi001_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <!-- ANWB Paddenstoel -->
        <Rule>
          <Name>ANWB Paddenstoel</Name>
          <Title>ANWB Paddenstoel</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi002_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Attractie -->
        <Rule>
          <Name>Attractie</Name>
          <Title>Attractie</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi003_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Berijdbaar voor brandweer -->
        <Rule>
          <Name>Berijdbaar voor brandweer</Name>
          <Title>Berijdbaar voor brandweer</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi004_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Bivakplaats Defensie -->
        <Rule>
          <Name>Bivakplaats Defensie</Name>
          <Title>Bivakplaats Defensie</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi005_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Bungalowpark -->
        <Rule>
          <Name>Bungalowpark</Name>
          <Title>Bungalowpark</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi010_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Calamiteiten coördinatiecentrum -->
        <Rule>
          <Name>Calamiteiten coördinatiecentrum</Name>
          <Title>Calamiteiten coördinatiecentrum</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi011_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Camping -->
        <Rule>
          <Name>Camping</Name>
          <Title>Camping</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi012_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Doorrijhoogte -->
        <Rule>
          <Name>Doorrijhoogte</Name>
          <Title>Doorrijhoogte</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi014_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Ecoduct -->
        <Rule>
          <Name>Ecoduct</Name>
          <Title>Ecoduct</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi015_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Feesttent -->
        <Rule>
          <Name>Feesttent</Name>
          <Title>Feesttent</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi016_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Heli landingsplaats -->
        <Rule>
          <Name>Heli landingsplaats</Name>
          <Title>Heli landingsplaats</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi018_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Hotel -->
        <Rule>
          <Name>Hotel</Name>
          <Title>Hotel</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi019_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Kleedkamer -->
        <Rule>
          <Name>Kleedkamer</Name>
          <Title>Kleedkamer</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi020_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Kraam elektra -->
        <Rule>
          <Name>Kraam elektra</Name>
          <Title>Kraam elektra</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi021_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Kraam gas -->
        <Rule>
          <Name>Kraam gas</Name>
          <Title>Kraam gas</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi022_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Mountainbike route -->
        <Rule>
          <Name>Mountainbike route</Name>
          <Title>Mountainbike route</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi023_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Object vitale infrastructuur -->
        <Rule>
          <Name>Object vitale infrastructuur</Name>
          <Title>Object vitale infrastructuur</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi024_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Omvormer -->
        <Rule>
          <Name>Omvormer</Name>
          <Title>Omvormer</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi025_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Opstapplaats RPA -->
        <Rule>
          <Name>Opstapplaats RPA</Name>
          <Title>Opstapplaats RPA</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi027_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Overdrachtsplaats ambulance-vervoer -->
        <Rule>
          <Name>Overdrachtsplaats ambulance-vervoer</Name>
          <Title>Overdrachtsplaats ambulance-vervoer</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi028_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Parkeerplaats -->
        <Rule>
          <Name>Parkeerplaats</Name>
          <Title>Parkeerplaats</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi029_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Passeerplaats -->
        <Rule>
          <Name>Passeerplaats</Name>
          <Title>Passeerplaats</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi030_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Restaurant -->
        <Rule>
          <Name>Restaurant</Name>
          <Title>Restaurant</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi032_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Rustplaats -->
        <Rule>
          <Name>Rustplaats</Name>
          <Title>Rustplaats</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi033_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Sleutelpaal of ringpaal -->
        <Rule>
          <Name>Sleutelpaal of ringpaal</Name>
          <Title>Sleutelpaal of ringpaal</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi034_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Solitair bouwwerk -->
        <Rule>
          <Name>Solitair bouwwerk</Name>
          <Title>Solitair bouwwerk</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi037_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Solitair bouwwerk risicogevend -->
        <Rule>
          <Name>Solitair bouwwerk risicogevend</Name>
          <Title>Solitair bouwwerk risicogevend</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi035_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Solitair bouwwerk, risico-ontvangend -->
        <Rule>
          <Name>Solitair bouwwerk, risico-ontvangend</Name>
          <Title>Solitair bouwwerk, risico-ontvangend</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi036_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Straattheater -->
        <Rule>
          <Name>Straattheater</Name>
          <Title>Straattheater</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi038_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Strandpaal, paal -->
        <Rule>
          <Name>Strandpaal, paal</Name>
          <Title>Strandpaal, paal</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi039_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Stuwrichting ventilaties -->
        <Rule>
          <Name>Stuwrichting ventilaties</Name>
          <Title>Stuwrichting ventilaties</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi040_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Uitzichtpunt -->
        <Rule>
          <Name>Uitzichtpunt</Name>
          <Title>Uitzichtpunt</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi041_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Verboden voor heli’s om te landen -->
        <Rule>
          <Name>Verboden voor heli’s om te landen</Name>
          <Title>Verboden voor heli’s om te landen</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi042_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Vuurhaard -->
        <Rule>
          <Name>Vuurhaard</Name>
          <Title>Vuurhaard</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi043_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Vuurwerkafsteekplaats -->
        <Rule>
          <Name>Vuurwerkafsteekplaats</Name>
          <Title>Vuurwerkafsteekplaats</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi044_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Wegafsluiting -->
        <Rule>
          <Name>Wegafsluiting</Name>
          <Title>Wegafsluiting</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi046_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Wegafsluiting passeerbaar -->
        <Rule>
          <Name>Wegafsluiting passeerbaar</Name>
          <Title>Wegafsluiting passeerbaar</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi045_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Wildrooster -->
        <Rule>
          <Name>Wildrooster</Name>
          <Title>Wildrooster</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi047_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Windvaan -->
        <Rule>
          <Name>Windvaan</Name>
          <Title>Windvaan</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi048_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Zendmast -->
        <Rule>
          <Name>Zendmast</Name>
          <Title>Zendmast</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi049_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Zittafel -->
        <Rule>
          <Name>Zittafel</Name>
          <Title>Zittafel</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi050_a.svg"/>
                <Format>image/svg+xml</Format>
              </ExternalGraphic>
              <Size>32</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>

        <!-- Zwaartepunt -->
        <Rule>
          <Name>Zwaartepunt</Name>
          <Title>Zwaartepunt</Title>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo><ogc:Literal>0</ogc:Literal><ogc:Literal>1</ogc:Literal></ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <ExternalGraphic>
                <OnlineResource xlink:href="./symbols/svg/poi051_a.svg"/>
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
