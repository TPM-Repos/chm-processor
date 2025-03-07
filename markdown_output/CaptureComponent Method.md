Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CaptureComponent Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CaptureComponent( _
       ByVal _componentPath_ As String, _
       ByVal _componentType_ As SolidWorks.Interop.swconst.swDocumentTypes_e _
    ) As ComponentHandle  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


