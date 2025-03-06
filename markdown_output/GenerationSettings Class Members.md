![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
GenerationSettings Class Members   
See Also Properties Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15238.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) : GenerationSettings Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [GenerationSettings](topic15238.md).

# ![](dotnetimages/collapse.gif)Public Constructors

| Name| Description  
---|---|---  
![Public Constructor](dotnetimages/publicConstructor.gif)| [GenerationSettings Constructor](topic15244.md)|   
Top

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [AutoExportAdditionalSheetFileFormats](topic15246.md)| Gets/Sets whether to automatically export additional sheet file formats.   
![Public Property](dotnetimages/publicProperty.gif)| [BatchActionInstancesAndComponents](topic15247.md)| Gets/sets whether instances and components are deleted, suppressed, unsuppressed, hidden, or shown in batches.   
![Public Property](dotnetimages/publicProperty.gif)| [CloseModelAfterGeneration](topic15248.md)| Determines whether the model should be closed after generation has completed.   
![Public Property](dotnetimages/publicProperty.gif)| [CreateEDrawingsHtml](topic15249.md)| Gets/sets whether HTML versions are created of each eDrawing that is generated.   
![Public Property](dotnetimages/publicProperty.gif)| [DefaultSpecificationFolder](topic15250.md)| Gets the default specification folder.   
![Public Property](dotnetimages/publicProperty.gif)| [DriveCustomPropertiesInAllConfigurations](topic15251.md)| Gets/sets whether custom properties should be driven in to all configurations.   
![Public Property](dotnetimages/publicProperty.gif)| [DxfExportPath](topic15252.md)| Gets/sets the path to a folder to which all exported DXFs should be saved, or a null reference to save them to the same location as their drawings.   
![Public Property](dotnetimages/publicProperty.gif)| [FeatureDeleteDisabled](topic15253.md)| Gets or sets whether feature deletion is disabled. If feature deletion is disabled then features which should be deleted will be suppressed instead. This property is not locked.   
![Public Property](dotnetimages/publicProperty.gif)| [FeatureDriveCompatibilityVersion](topic15254.md)| Gets/sets the compatibility version used to drive feature parameters, 0 means to drive features in the exact way as DriveWorks 7 and 8, 1 means to drive features using DriveWorks 9's semantics - i.e. Hole Wizard features are driven using user units rather than system units.   
![Public Property](dotnetimages/publicProperty.gif)| [Group](topic15255.md)| Gets the current group.   
![Public Property](dotnetimages/publicProperty.gif)| [GroupContentFolder](topic15256.md)| Gets the folder used to locate group content.   
![Public Property](dotnetimages/publicProperty.gif)| [IsLocked](topic15257.md)| Determines whether the object has been locked.   
![Public Property](dotnetimages/publicProperty.gif)| [IsSpr542635WorkAroundEnabled](topic15258.md)| Gets/sets whether the SPR542635 work around is enabled.   
![Public Property](dotnetimages/publicProperty.gif)| [MinimumReportingLevel](topic15259.md)| Gets/sets minimum reporting level that will be used during generation. Anything below this level will not be stored in the group report.   
![Public Property](dotnetimages/publicProperty.gif)| [OverwriteReleasedComponentData](topic15260.md)| Gets/sets whether existing released components are overwritten.   
![Public Property](dotnetimages/publicProperty.gif)| [SharedContentFolder](topic15261.md)| Gets the folder used to locate shared content.   
![Public Property](dotnetimages/publicProperty.gif)| [SupportLegacyMaterialCustomProperties](topic15262.md)| Gets/sets whether legacy color and material custom properties are supported.   
![Public Property](dotnetimages/publicProperty.gif)| [UseZoomToFit](topic15263.md)| Gets/sets whether or not models and drawings will be zoomed to fit during generation.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [Load](topic15245.md)| Loads settings from the specified group.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GenerationSettings Class](topic15238.md)   
[DriveWorks.SolidWorks.Generation Namespace](topic15094.md)


