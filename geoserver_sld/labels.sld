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
              <ogc:PropertyName>soort</ogc:PropertyName>
              <ogc:Literal>Algemeen</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>10000</MaxScaleDenominator>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label><ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
            <VendorOption name="graphic-resize">stretch</VendorOption>                        
            <VendorOption name="graphic-margin">0.7</VendorOption> 
          </TextSymbolizer>
        </Rule>-->
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
             <ogc:PropertyName>soort</ogc:PropertyName>
              <ogc:Literal>Gevaar</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>10000</MaxScaleDenominator>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label><ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
              <CssParameter name="font-style">normal</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
                <Rotation>
                  <ogc:PropertyName>rotatie</ogc:PropertyName>
                </Rotation>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill">#ffffff</CssParameter>
              <CssParameter name="fill-opacity">1</CssParameter> 
            </Fill> 
            <VendorOption name="conflictResolution">false</VendorOption>
          </TextSymbolizer>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label><ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
      ]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function><![CDATA[      ]]></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
              <CssParameter name="font-style">bold</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
                <Rotation>
                  <ogc:PropertyName>rotatie</ogc:PropertyName>
                </Rotation>
              </PointPlacement>
            </LabelPlacement>
            <Fill>
              <CssParameter name="fill-opacity">0</CssParameter> 
            </Fill> 
            <Graphic>
              <Mark>
                <WellKnownName>square</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#ff0000</CssParameter>    
                  <CssParameter name="fill-opacity">1</CssParameter>              
                </Fill>
                <Stroke>
                  <CssParameter name="stroke">#000000</CssParameter>    
                  <CssParameter name="stroke-width">0.2</CssParameter>               
                </Stroke>
              </Mark>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
            <VendorOption name="graphic-resize">stretch</VendorOption>                        
            <VendorOption name="graphic-margin">0.7</VendorOption> 
          </TextSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>soort</ogc:PropertyName>
              <ogc:Literal>Voorzichtig</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>10000</MaxScaleDenominator>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label><ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
            <VendorOption name="conflictResolution">false</VendorOption>
          </TextSymbolizer>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label><ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
      ]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function><![CDATA[      ]]></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
              <CssParameter name="fill-opacity">0</CssParameter> 
            </Fill> 
            <Graphic>
              <Mark>
                <WellKnownName>square</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#ffff00</CssParameter>
                  <CssParameter name="fill-opacity">1</CssParameter>            
                </Fill>
                <Stroke>
                  <CssParameter name="stroke">#000000</CssParameter>
                  <CssParameter name="stroke-width">0.2</CssParameter> 
                </Stroke>
              </Mark>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
            <VendorOption name="graphic-resize">stretch</VendorOption>                        
            <VendorOption name="graphic-margin">0.7</VendorOption> 
          </TextSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>soort</ogc:PropertyName>
              <ogc:Literal>Waarschuwing</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>10000</MaxScaleDenominator>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label><ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
            <VendorOption name="conflictResolution">false</VendorOption>
          </TextSymbolizer>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label><ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
      ]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function><![CDATA[      ]]></Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
              <CssParameter name="fill-opacity">0</CssParameter>
            </Fill> 
            <Graphic>
              <Mark>
                <WellKnownName>square</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#ffcc00</CssParameter>  
                  <CssParameter name="fill-opacity">1</CssParameter>       
                </Fill>
                <Stroke>
                  <CssParameter name="stroke">#000000</CssParameter>    
                  <CssParameter name="stroke-width">0.2</CssParameter>
                </Stroke>
              </Mark>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
            <VendorOption name="graphic-resize">stretch</VendorOption>                         
            <VendorOption name="graphic-margin">0.7</VendorOption> 
          </TextSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>soort</ogc:PropertyName>
              <ogc:Literal>publieke ingang</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>10000</MaxScaleDenominator>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label>
              <ogc:Function name="Concatenate">
                <ogc:Literal>INGANG </ogc:Literal>
                <ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function>
              </ogc:Function>
            </Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
            <VendorOption name="conflictResolution">false</VendorOption>
          </TextSymbolizer>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label>
              <ogc:Function name="Concatenate">
                <ogc:Literal>INGANG </ogc:Literal>
                <ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function>
              </ogc:Function>
            </Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
              <CssParameter name="fill-opacity">0</CssParameter> 
            </Fill> 
            <Graphic>
              <Mark>
                <WellKnownName>square</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#08a6f5</CssParameter>
                  <CssParameter name="fill-opacity">1</CssParameter>            
                </Fill>
                <Stroke>
                  <CssParameter name="stroke">#08a6f5</CssParameter>
                  <CssParameter name="stroke-width">0.2</CssParameter> 
                </Stroke>
              </Mark>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
            <VendorOption name="graphic-resize">stretch</VendorOption>                        
            <VendorOption name="graphic-margin">0.7</VendorOption> 
          </TextSymbolizer>
        </Rule> 
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>soort</ogc:PropertyName>
              <ogc:Literal>calamiteitendoorgang</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <MaxScaleDenominator>10000</MaxScaleDenominator>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label>
              <ogc:Function name="Concatenate">
                <ogc:Literal>CADO </ogc:Literal>
                <ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function>
              </ogc:Function>
            </Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
            <VendorOption name="conflictResolution">false</VendorOption>
          </TextSymbolizer>
          <TextSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <Label>
              <ogc:Function name="Concatenate">
                <ogc:Literal>CADO </ogc:Literal>
                <ogc:Function name="strReplace"><ogc:PropertyName>omschrijving</ogc:PropertyName><ogc:Literal>\\</ogc:Literal><ogc:Literal><![CDATA[
]]></ogc:Literal><ogc:Literal>true</ogc:Literal></ogc:Function>
              </ogc:Function>
            </Label>
            <Font>
              <CssParameter name="font-family">Arial</CssParameter>
              <CssParameter name="font-size">3</CssParameter>
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
              <CssParameter name="fill-opacity">0</CssParameter> 
            </Fill> 
            <Graphic>
              <Mark>
                <WellKnownName>square</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#e31a1c</CssParameter>
                  <CssParameter name="fill-opacity">1</CssParameter>            
                </Fill>
                <Stroke>
                  <CssParameter name="stroke">#e31a1c</CssParameter>
                  <CssParameter name="stroke-width">0.2</CssParameter> 
                </Stroke>
              </Mark>
              <Rotation>
                <ogc:PropertyName>rotatie</ogc:PropertyName>
              </Rotation>
            </Graphic>
            <VendorOption name="graphic-resize">stretch</VendorOption>                        
            <VendorOption name="graphic-margin">0.7</VendorOption> 
          </TextSymbolizer>
        </Rule>              
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>