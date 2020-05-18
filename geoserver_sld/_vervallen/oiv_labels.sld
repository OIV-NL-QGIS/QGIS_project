<?xml version="1.0" encoding="UTF-8"?>

<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd">
  <NamedLayer>
    <Name>Labels</Name>
    <UserStyle>
      <Name>labels</Name>
      <FeatureTypeStyle>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>type_label</ogc:PropertyName>
              <ogc:Literal>Algemeen</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>1000</MaxScaleDenominator>
          <TextSymbolizer>
            <Label>
              <ogc:PropertyName>omschrijving</ogc:PropertyName>
            </Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">12.0</CssParameter>
              <CssParameter name="font-style">normal</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
                <Displacement>
                  <DisplacementX>0</DisplacementX>
                  <DisplacementY>0</DisplacementY>
                </Displacement>
                <Rotation>
                  <ogc:PropertyName>rotatie</ogc:PropertyName>
                </Rotation>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill> 
            <VendorOption name="graphic-resize">stretch</VendorOption>                        
            <VendorOption name="graphic-margin">2</VendorOption> 
          </TextSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>type_label</ogc:PropertyName>
              <ogc:Literal>Gevaar</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>1000</MaxScaleDenominator>
          <TextSymbolizer>
            <Label>
              <ogc:PropertyName>omschrijving</ogc:PropertyName>
            </Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">12.0</CssParameter>
              <CssParameter name="font-style">normal</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
                <Displacement>
                  <DisplacementX>0</DisplacementX>
                  <DisplacementY>0</DisplacementY>
                </Displacement>
                <Rotation>
                  <ogc:PropertyName>rotatie</ogc:PropertyName>
                </Rotation>>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#ffffff</CssParameter>
            </Fill> 
            <Graphic>
              <Mark>
                <WellKnownName>square</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#ff0000</CssParameter>                 
                </Fill>
                <Stroke>
                  <CssParameter name="stroke">#000000</CssParameter>                 
                </Stroke>
              </Mark>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
            <VendorOption name="graphic-resize">stretch</VendorOption>                        
            <VendorOption name="graphic-margin">2</VendorOption> 
          </TextSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>type_label</ogc:PropertyName>
              <ogc:Literal>Voorzichtig</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>1000</MaxScaleDenominator>
          <TextSymbolizer>
            <Label>
              <ogc:PropertyName>omschrijving</ogc:PropertyName>
            </Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">12.0</CssParameter>
              <CssParameter name="font-style">normal</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
                <Displacement>
                  <DisplacementX>0</DisplacementX>
                  <DisplacementY>0</DisplacementY>
                </Displacement>
                <Rotation>
                  <ogc:PropertyName>rotatie</ogc:PropertyName>
                </Rotation>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill> 
            <Graphic>
              <Mark>
                <WellKnownName>square</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#ffff00</CssParameter>                 
                </Fill>
                <Stroke>
                  <CssParameter name="stroke">#000000</CssParameter>                 
                </Stroke>
              </Mark>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
            <VendorOption name="graphic-resize">stretch</VendorOption>                        
            <VendorOption name="graphic-margin">2</VendorOption> 
          </TextSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>type_label</ogc:PropertyName>
              <ogc:Literal>Waarschuwing</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>1000</MaxScaleDenominator>
          <TextSymbolizer>
            <Label>
              <ogc:PropertyName>omschrijving</ogc:PropertyName>
            </Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">12.0</CssParameter>
              <CssParameter name="font-style">normal</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
                <Displacement>
                  <DisplacementX>0</DisplacementX>
                  <DisplacementY>0</DisplacementY>
                </Displacement>
                <Rotation>
                  <ogc:PropertyName>rotatie</ogc:PropertyName>
                </Rotation>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
              <CssParameter name="fill-opacity">1</CssParameter>
            </Fill> 
            <Graphic>
              <Mark>
                <WellKnownName>square</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#ffcc00</CssParameter>                 
                </Fill>
                <Stroke>
                  <CssParameter name="stroke">#000000</CssParameter>                 
                </Stroke>
              </Mark>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
            <VendorOption name="graphic-resize">stretch</VendorOption>                         
            <VendorOption name="graphic-margin">2</VendorOption> 
          </TextSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>