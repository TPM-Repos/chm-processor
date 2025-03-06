       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TrySaveTemporaryFile Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13594.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : TrySaveTemporaryFile Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_temporaryLocation_
    The full path to a temporary location where the file will be saved.

_options_
    The options to use during save.

_exportData_
    Optionally, the export data needed during the save.

Glossary Item Box

Attempts to save the file to the specified temporary location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function TrySaveTemporaryFile( _
       ByVal _temporaryLocation_ As String, _
       ByVal _options_ As SolidWorks.Interop.swconst.swSaveAsOptions_e, _
       Optional ByVal _exportData_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim temporaryLocation As String
    Dim options As SolidWorks.Interop.swconst.swSaveAsOptions_e
    Dim exportData As Object
    Dim value As Boolean
     
    value = instance.TrySaveTemporaryFile(temporaryLocation, options, exportData)  
  
C#|   
---|---  
      
    
    protected virtual bool TrySaveTemporaryFile( 
       string _temporaryLocation_ ,
       SolidWorks.Interop.swconst.swSaveAsOptions_e _options_ ,
       object _exportData_
    )  
  
#### Parameters

 _temporaryLocation_
    The full path to a temporary location where the file will be saved.
_options_
    The options to use during save.
_exportData_
    Optionally, the export data needed during the save.

#### Return Value

True if the file was saved in the location successfully, otherwise False.

# Remarks

This temporary file will then be copied to its final destination as part of the TrySaveAs method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)

©2024 DriveWorks Ltd. All Rights Reserved.
