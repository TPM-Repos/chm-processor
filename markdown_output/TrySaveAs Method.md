TrySaveAs Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : TrySaveAs Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_targetPath_
    The path to save the model to.

_options_
    The options to use during save.

_exportData_
    

Glossary Item Box

Helper method that will attempt to save the current model with the specified path and options. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function TrySaveAs( _
       ByVal _targetPath_ As String, _
       ByVal _options_ As SolidWorks.Interop.swconst.swSaveAsOptions_e, _
       Optional ByVal _exportData_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim targetPath As String
    Dim options As SolidWorks.Interop.swconst.swSaveAsOptions_e
    Dim exportData As Object
    Dim value As Boolean
     
    value = instance.TrySaveAs(targetPath, options, exportData)  
  
C#|   
---|---  
      
    
    protected bool TrySaveAs( 
       string _targetPath_ ,
       SolidWorks.Interop.swconst.swSaveAsOptions_e _options_ ,
       object _exportData_
    )  
  
#### Parameters

 _targetPath_
    The path to save the model to.
_options_
    The options to use during save.
_exportData_
    

#### Return Value

True if the save was successful.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)


