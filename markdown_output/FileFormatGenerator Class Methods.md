Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
FileFormatGenerator Class Methods   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : FileFormatGenerator Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [FileFormatGenerator members](topic13580.md).

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

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


