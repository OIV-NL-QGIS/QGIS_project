<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:se="http://www.opengis.net/se" version="1.1.0">
  <NamedLayer>
    <se:Name>Installatietechnische veiligheidsvoorzieningen</se:Name>
    <UserStyle>
      <se:Name>Installatietechnische veiligheidsvoorzieningen</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>Afsluiter CV</se:Name>
          <se:Description>
            <se:Title>Afsluiter CV</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>7</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_cv.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>8</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_elektra.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>9</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_gas.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>11</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_neon.png"/>
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
          <se:Name>Afsluiter omloop</se:Name>
          <se:Description>
            <se:Title>Afsluiter omloop</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>13</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_omloop.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>14</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_rwa.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>15</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_sprinkler.png"/>
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
          <se:Name>Afsluiter water</se:Name>
          <se:Description>
            <se:Title>Afsluiter water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>16</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_water.png"/>
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
          <se:Name>Blussysteem gas</se:Name>
          <se:Description>
            <se:Title>Blussysteem gas</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>23</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/blussysteem_koolstofdioxide.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>25</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/blussysteem_schuim.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>26</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/blussysteem_water.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>30</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/brandmeldpaneel.png"/>
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
          <se:Name>Noodstop</se:Name>
          <se:Description>
            <se:Title>Noodstop</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>12</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/noodstop.png"/>
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
          <se:Name>Rook warmte afvoer</se:Name>
          <se:Description>
            <se:Title>Rook warmte afvoer</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>147</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/rookwarmte_afvoer.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>151</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/stijgleiding_hd_afnamepunt.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>152</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/stijgleiding_hd_vulpunt.png"/>
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
          <se:Name>Stijgleiding LD afnamepunt</se:Name>
          <se:Description>
            <se:Title>Stijgleiding LD afnamepunt</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>149</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/stijgleiding_ld_afnamepunt.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>150</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/stijgleiding_ld_vulpunt.png"/>
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
          <se:Name>Meterkast electra en gas</se:Name>
          <se:Description>
            <se:Title>Meterkast electra en gas</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>156</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/meterkast_e_g.png"/>
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
          <se:Name>Meterkast electra en water</se:Name>
          <se:Description>
            <se:Title>Meterkast electra en water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>157</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/meterkast_e_w.png"/>
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
          <se:Name>Meterkast gas en water</se:Name>
          <se:Description>
            <se:Title>Meterkast gas en water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>158</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/meterkast_g_w.png"/>
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
          <se:Name>Meterkast electra, gas en water</se:Name>
          <se:Description>
            <se:Title>Meterkast electra, gas en water</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>159</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/meterkast_e_g_w.png"/>
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
          <se:Name>Brandmeldcentrale</se:Name>
          <se:Description>
            <se:Title>Brandmeldcentrale</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>162</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/brandmeldcentrale.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>163</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/ontruimingspaneel.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>164</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/afsluiter_luchtbehandeling.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>171</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/blussysteem_hifog.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>172</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/blussysteem_AFFF.png"/>
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
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>161</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/nevenpaneel.png"/>
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
          <se:Name>Activering blussysteem</se:Name>
          <se:Description>
            <se:Title>Activering blussysteem</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>1001</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/activering_blussysteem.png"/>
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
          <se:Name>Brandblusser</se:Name>
          <se:Description>
            <se:Title>Brandblusser</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>1002</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/brandblusser.png"/>
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
          <se:Name>Brandslanghaspel</se:Name>
          <se:Description>
            <se:Title>Brandslanghaspel</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>1003</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/brandslanghaspel.png"/>
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
          <se:Name>Oogdouche</se:Name>
          <se:Description>
            <se:Title>Oogdouche</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>1004</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/oogdouche.png"/>
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
          <se:Name>Nooddouche</se:Name>
          <se:Description>
            <se:Title>Nooddouche</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>veiligh_install_type_id</ogc:PropertyName>
              <ogc:Literal>1005</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>2500</se:MaxScaleDenominator>
          <se:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <se:Graphic>
              <se:ExternalGraphic>
                <se:OnlineResource xlink:type="simple" xlink:href="./oiv/nooddouche.png"/>
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
