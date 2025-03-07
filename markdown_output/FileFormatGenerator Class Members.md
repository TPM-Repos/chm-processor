Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
FileFormatGenerator Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13579.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : FileFormatGenerator Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [FileFormatGenerator](topic13579.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [FullGenerationPath](topic13597.md)| Gets/sets the path of the additional file that is generated.   
![Public Property](dotnetimages/publicProperty.gif)| [Parameters](topic13599.md)| Gets all parameters for this file format that can be captured.   
![Public Property](dotnetimages/publicProperty.gif)| [TemporaryDirectory](topic13603.md)| Gets/sets the temporary directory used during generation.   
Top

# Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [DefaultProperties](topic13595.md)| Gets a collection of default properties that should be used when inheriting this class.   
![Protected Property](dotnetimages/protectedProperty.gif)| [FormatData](topic13596.md)| Gets/sets the released format data (rules etc) for the additional file.   
![Protected Property](dotnetimages/protectedProperty.gif)| [OriginalModelPath](topic13598.md)| Gets/sets the path of the model that the additional file will be generated from.   
![Protected Property](dotnetimages/protectedProperty.gif)| [Report](topic13600.md)| Gets/sets the report writer to use during generation process.   
![Protected Property](dotnetimages/protectedProperty.gif)| [Settings](topic13601.md)| Gets/sets the generation settings that should be used.   
![Protected Property](dotnetimages/protectedProperty.gif)| [TargetModel](topic13602.md)| Gets/sets the target model that the additional file is created from.   
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| [Generate](topic13585.md)| Generates the file format and any additional files too.   
Public Method| [GetParameters](topic13586.md)| Gets all parameters that should be captured for a particular component.   
Public Method| [PrepareGeneration](topic13588.md)| Overloaded. Called before main generation, should be used to initialize and evaluate parameters to determine if generation can take place.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [OnAdditionalFileGenerated](topic13587.md)| Raises the [AdditionalFileGenerated](topic13606.md) event.   
Protected Method| [TryGenerateFilePath](topic13591.md)| Helper method for using the "File Name" parameter value to create a new path.   
Protected Method| [TryGenerateRelativePath](topic13592.md)| Helper method for using the "Relative Path" parameter value to create a new path.   
Protected Method| [TrySaveAs](topic13593.md)| Helper method that will attempt to save the current model with the specified path and options.   
Protected Method| [TrySaveTemporaryFile](topic13594.md)| Attempts to save the file to the specified temporary location.   
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [AdditionalFileCopied](topic13604.md)| Raised when the additional file format has been copied to the target location.   
![Public Event](dotnetimages/publicEvent.gif)| [AdditionalFileCopying](topic13605.md)| Raised before the additional file format is copied to the target location.   
![Public Event](dotnetimages/publicEvent.gif)| [AdditionalFileGenerated](topic13606.md)| Raised when an additional file format is saved.   
Top

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


