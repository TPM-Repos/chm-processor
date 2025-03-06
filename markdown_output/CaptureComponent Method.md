![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CaptureComponent Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13390.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : CaptureComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentPath_
    The path to the component to capture.

_componentType_
    The type of the component to capture.

Glossary Item Box

Captures the component with the given path. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CaptureComponent( _
       ByVal _componentPath_ As String, _
       ByVal _componentType_ As SolidWorks.Interop.swconst.swDocumentTypes_e _
    ) As ComponentHandle  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim componentPath As String
    Dim componentType As SolidWorks.Interop.swconst.swDocumentTypes_e
    Dim value As ComponentHandle
     
    value = instance.CaptureComponent(componentPath, componentType)  
  
C#|   
---|---  
      
    
    ComponentHandle CaptureComponent( 
       string _componentPath_ ,
       SolidWorks.Interop.swconst.swDocumentTypes_e _componentType_
    )  
  
#### Parameters

 _componentPath_
    The path to the component to capture.
_componentType_
    The type of the component to capture.

#### Return Value

A handle to the captured component.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)

©2024 DriveWorks Ltd. All Rights Reserved.
