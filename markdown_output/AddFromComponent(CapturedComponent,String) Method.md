![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddFromComponent(CapturedComponent,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2476.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [CaptureImportManager Class](topic2468.md) > [AddFromComponent Method](topic2474.md) : AddFromComponent(CapturedComponent,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The component to add.

_newPath_
    The new master path of the component.

Glossary Item Box

Adds the given component to the collection of components to import, and changes it's master path to the new path given. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub AddFromComponent( _
       ByVal _component_ As [CapturedComponent](topic6147.md), _
       ByVal _newPath_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CaptureImportManager](topic2468.md)
    Dim component As [CapturedComponent](topic6147.md)
    Dim newPath As String
     
    instance.AddFromComponent(component, newPath)  
  
C#|   
---|---  
      
    
    public void AddFromComponent( 
       [CapturedComponent](topic6147.md) _component_ ,
       string _newPath_
    )  
  
#### Parameters

 _component_
    The component to add.
_newPath_
    The new master path of the component.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CaptureImportManager Class](topic2468.md)   
[CaptureImportManager Members](topic2469.md)   
[Overload List](topic2474.md)

©2024 DriveWorks Ltd. All Rights Reserved.
