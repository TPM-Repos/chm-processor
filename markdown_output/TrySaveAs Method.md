![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TrySaveAs Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13593.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function TrySaveAs( _
       ByVal _targetPath_ As String, _
       ByVal _options_ As SolidWorks.Interop.swconst.swSaveAsOptions_e, _
       Optional ByVal _exportData_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)

©2024 DriveWorks Ltd. All Rights Reserved.
