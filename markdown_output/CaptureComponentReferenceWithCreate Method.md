Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CaptureComponentReferenceWithCreate Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : CaptureComponentReferenceWithCreate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_parentHandle_
    Handle to the parent in which to capture the component.

_childPath_
    The path to the component to capture.

_childType_
    The type of the component to capture.

Glossary Item Box

Captures the component with the given path and adds it as a child to the given parent. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CaptureComponentReferenceWithCreate( _
       ByVal _parentHandle_ As ComponentHandle, _
       ByVal _childPath_ As String, _
       ByVal _childType_ As SolidWorks.Interop.swconst.swDocumentTypes_e _
    ) As ComponentHandle  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim parentHandle As ComponentHandle
    Dim childPath As String
    Dim childType As SolidWorks.Interop.swconst.swDocumentTypes_e
    Dim value As ComponentHandle
     
    value = instance.CaptureComponentReferenceWithCreate(parentHandle, childPath, childType)  
  
C#|   
---|---  
      
    
    ComponentHandle CaptureComponentReferenceWithCreate( 
       ComponentHandle _parentHandle_ ,
       string _childPath_ ,
       SolidWorks.Interop.swconst.swDocumentTypes_e _childType_
    )  
  
#### Parameters

 _parentHandle_
    Handle to the parent in which to capture the component.
_childPath_
    The path to the component to capture.
_childType_
    The type of the component to capture.

#### Return Value

A handle to the captured component

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


