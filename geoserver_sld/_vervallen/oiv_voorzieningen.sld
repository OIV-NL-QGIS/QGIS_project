<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:se="http://www.opengis.net/se">
  <NamedLayer>
    <se:Name>voorziening</se:Name>
    <UserStyle>
      <se:Name>voorziening</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>Afsluiter CV</se:Name>
          <se:Description>
            <se:Title>Afsluiter CV</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter CV</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_cv.png"/>
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
          <se:Name>Afsluiter gas</se:Name>
          <se:Description>
            <se:Title>Afsluiter gas</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter gas</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_gas.png"/>
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
          <se:Name>Afsluiter neon</se:Name>
          <se:Description>
            <se:Title>Afsluiter neon</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter neon</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_neon.png"/>
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
          <se:Name>Afsluiter noodstop</se:Name>
          <se:Description>
            <se:Title>Afsluiter noodstop</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter noodstop</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_noodstop.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Afsluiter omloop</se:Name>
          <se:Description>
            <se:Title>Afsluiter omloop</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter omloop</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_omloop.png"/>
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
          <se:Name>Afsluiter RWA</se:Name>
          <se:Description>
            <se:Title>Afsluiter RWA</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter RWA</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_rwa.png"/>
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
          <se:Name>Afsluiter sprinkler</se:Name>
          <se:Description>
            <se:Title>Afsluiter sprinkler</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter sprinkler</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_sprinkler.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size><se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Afsluiter water</se:Name>
          <se:Description>
            <se:Title>Afsluiter water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter water</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_water.png"/>
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
          <se:Name>Asbest</se:Name>
          <se:Description>
            <se:Title>Asbest</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Asbest</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/asbest.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Bereik DMO</se:Name>
          <se:Description>
            <se:Title>Bereik DMO</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Bereik DMO</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/dekkingsprobleem_dmo.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Bereik TMO</se:Name>
          <se:Description>
            <se:Title>Bereik TMO</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Bereik TMO</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/dekkingsprobleem_tmo.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Biologische agentia</se:Name>
          <se:Description>
            <se:Title>Biologische agentia</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Biologische agentia</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/biologische_agentia.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Blussysteem gas</se:Name>
          <se:Description>
            <se:Title>Blussysteem gas</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Blussysteem gas</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/blussysteem_koolstofdioxide.png"/>
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
          <se:Name>Blussysteem schuim</se:Name>
          <se:Description>
            <se:Title>Blussysteem schuim</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Blussysteem schuim</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/blussysteem_schuim.png"/>
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
          <se:Name>Blussysteem water</se:Name>
          <se:Description>
            <se:Title>Blussysteem water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Blussysteem water</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/blussysteem_water.png"/>
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
          <se:Name>Brandmeldpaneel</se:Name>
          <se:Description>
            <se:Title>Brandmeldpaneel</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Brandmeldpaneel</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/brandmeldpaneel.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>2</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
             </se:Rotation>
 	 </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Brandweeringang</se:Name>
          <se:Description>
            <se:Title>Brandweeringang</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Brandweeringang</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" 
                                   xlink:href="./png/oiv/objecten/brandweeringang.png"/>
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
          <se:Name>Brandweerlift</se:Name>
          <se:Description>
            <se:Title>Brandweerlift</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Brandweerlift</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/brandweerlift.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>2</se:Size>
		 <se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Elektrische spanning</se:Name>
          <se:Description>
            <se:Title>Elektrische spanning</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Elektrische spanning</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/elektrische_spanning.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Lage temp of bevriezing</se:Name>
          <se:Description>
            <se:Title>Lage temp of bevriezing</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Lage temp of bevriezing</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/lage_temperatuur.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Laser straal</se:Name>
          <se:Description>
            <se:Title>Laser straal</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Laser straal</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/laserstralen.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
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
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Magnetisch veld</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/magnetisch_veld.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
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
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Neveningang</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/neveningang.png"/>
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
          <se:Name>Niet-ioniserende straling</se:Name>
          <se:Description>
            <se:Title>Niet-ioniserende straling</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Niet-ioniserende straling</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/niet_ioniserende_straling.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
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
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Niet blussen met water</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/niet_blussen_met_water.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Opstelplaats overig</se:Name>
          <se:Description>
            <se:Title>Opstelplaats overig</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Opstelplaats overig</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/opstelplaats_overige_blusvoertuigen.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Radioactieve stof</se:Name>
          <se:Description>
            <se:Title>Radioactieve stof</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Radioactieve stof</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/radioactief_materiaal.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Rietenkap</se:Name>
          <se:Description>
            <se:Title>Rietenkap</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Rietenkap</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/rietenkap.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Rook warmte afvoer</se:Name>
          <se:Description>
            <se:Title>Rook warmte afvoer</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Rook warmte afvoer</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/rookwarmte_afvoer.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Sleutelkluis</se:Name>
          <se:Description>
            <se:Title>Sleutelkluis</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Sleutelkluis</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/sleutelkluis.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
	<se:Rule>
          <se:Name>Stijgleiding LD afnamepunt</se:Name>
          <se:Description>
            <se:Title>Stijgleiding LD afnamepunt</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Stijgleiding afnamepunt</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/stijgleiding_ld_afnamepunt.png"/>
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
          <se:Name>Stijgleiding LD vulpunt</se:Name>
          <se:Description>
            <se:Title>Stijgleiding LD vulpunt</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Stijgleiding vulpunt</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/stijgleiding_ld_vulpunt.png"/>
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
          <se:Name>Stijgleiding HD afnamepunt</se:Name>
          <se:Description>
            <se:Title>Stijgleiding HD afnamepunt</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Stijgleiding HD afnamepunt</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/stijgleiding_hd_afnamepunt.png"/>
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
          <se:Name>Stijgleiding HD vulpunt</se:Name>
          <se:Description>
            <se:Title>Stijgleiding HD vulpunt</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Stijgleiding HD vulpunt</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/stijgleiding_hd_vulpunt.png"/>
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
          <se:Name>Trap bordes</se:Name>
          <se:Description>
            <se:Title>Trap bordes</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Trap bordes</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/trap_bordes.png"/>
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
          <se:Name>Waterkanon</se:Name>
          <se:Description>
            <se:Title>Waterkanon</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Waterkanon</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/waterkanon.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Meterkast electra en gas</se:Name>
          <se:Description>
            <se:Title>Meterkast electra en gas</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Meterkast electra en gas</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/meterkast_e_g.png"/>
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
          <se:Name>Meterkast electra en water</se:Name>
          <se:Description>
            <se:Title>Meterkast electra en water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Meterkast electra en water</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/meterkast_e_w.png"/>
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
          <se:Name>Meterkast gas en water</se:Name>
          <se:Description>
            <se:Title>Meterkast gas en water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Meterkast gas en water</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/meterkast_g_w.png"/>
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
          <se:Name>Meterkast electra, gas en water</se:Name>
          <se:Description>
            <se:Title>Meterkast electra, gas en water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Meterkast electra, gas en water</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/meterkast_e_g_w.png"/>
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
          <se:Name>Verzamelplaats</se:Name>
          <se:Description>
            <se:Title>Verzamelplaats</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Verzamelplaats</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/verzamelplaats.png"/>
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
          <se:Name>Nevenbrandweerpaneel</se:Name>
          <se:Description>
            <se:Title>Nevenbrandweerpaneel</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Nevenbrandweerpaneel</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/nevenpaneel.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>2</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>

	<se:Rule>
          <se:Name>Brandmeldcentrale</se:Name>
          <se:Description>
            <se:Title>Brandmeldcentrale</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Brandmeldcentrale</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/brandmeldcentrale.png"/>
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
          <se:Name>Ontruimingspaneel</se:Name>
          <se:Description>
            <se:Title>Ontruimingspaneel</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Ontruimingspaneel</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/ontruimingspaneel.png"/>
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
          <se:Name>Afsluiter luchtbehandeling</se:Name>
          <se:Description>
            <se:Title>Afsluiter luchtbehandeling</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter luchtbehandeling</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_luchtbehandeling.png"/>
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
          <se:Name>Lift</se:Name>
          <se:Description>
            <se:Title>Lift</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Lift</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/lift.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>2</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
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
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Ontvlambare stoffen</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/ontvlambare_stoffen.png"/>
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
          <se:Name>Giftige stoffen</se:Name>
          <se:Description>
            <se:Title>Giftige stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Giftige stoffen</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/giftige_stoffen.png"/>
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
          <se:Name>Bijtende stoffen</se:Name>
          <se:Description>
            <se:Title>Bijtende stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Bijtende stoffen</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/bijtende_stoffen.png"/>
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
          <se:Name>Oxiderende stoffen</se:Name>
          <se:Description>
            <se:Title>Oxiderende stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Oxiderende stoffen</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/oxiderende_stoffen.png"/>
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
          <se:Name>Explosieve stoffen</se:Name>
          <se:Description>
            <se:Title>Explosieve stoffen</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Explosieve stoffen</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/explosieve_stoffen.png"/>
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
          <se:Name>Blussysteem Hi-Fog</se:Name>
          <se:Description>
            <se:Title>Blussysteem Hi-Fog</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Blussysteem Hi-Fog</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/blussysteem_hifog.png"/>
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
          <se:Name>Blussysteem AFFF</se:Name>
          <se:Description>
            <se:Title>Blussysteem AFFF</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Blussysteem AFFF</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/blussysteem_afff.png"/>
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
          <se:Name>Trap rond</se:Name>
          <se:Description>
            <se:Title>Trap rond</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Trap rond</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/trap_rond.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>3</se:Size>
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
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Trap recht</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/trap_recht.png"/>
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
          <se:Name>GEVI bord</se:Name>
          <se:Description>
            <se:Title>GEVI bord</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>GEVI bord</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/gevi_bord.png"/>
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
          <se:Name>Afsluiter electra</se:Name>
          <se:Description>
            <se:Title>Afsluiter electra</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>pictogram</ogc:PropertyName>
              <ogc:Literal>Afsluiter electra</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./png/oiv/objecten/afsluiter_elektra.png"/>
                <se:Format>image/png</se:Format>
              </se:ExternalGraphic>
              <se:Size>5</se:Size>
		<se:Rotation>
		<ogc:PropertyName>rotatie</ogc:PropertyName>
	     </se:Rotation>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
