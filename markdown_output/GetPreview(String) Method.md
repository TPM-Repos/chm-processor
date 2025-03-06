![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetPreview(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2271.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IPreviewDocument Interface](topic2263.md) > [GetPreview Method](topic2269.md) : GetPreview(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_lightPreset_
    Name of the lighting preset to apply.

Glossary Item Box

Generates the document and updates the preview result. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetPreview( _
       ByVal _lightPreset_ As String _
    ) As IDisposable  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IPreviewDocument](topic2263.md)
    Dim lightPreset As String
    Dim value As IDisposable
     
    value = instance.GetPreview(lightPreset)  
  
C#|   
---|---  
      
    
    IDisposable GetPreview( 
       string _lightPreset_
    )  
  
#### Parameters

 _lightPreset_
    Name of the lighting preset to apply.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IPreviewDocument Interface](topic2263.md)   
[IPreviewDocument Members](topic2264.md)   
[Overload List](topic2269.md)

©2024 DriveWorks Ltd. All Rights Reserved.
