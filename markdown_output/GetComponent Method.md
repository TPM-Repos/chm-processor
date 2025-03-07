Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponent Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : GetComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentHandle_
    A handle to the component for which to get capture data.

Glossary Item Box

Gets the captured component for the component with the given handle. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetComponent( _
       ByVal _componentHandle_ As ComponentHandle _
    ) As [CapturedSolidWorksComponent](topic14343.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim componentHandle As ComponentHandle
    Dim value As [CapturedSolidWorksComponent](topic14343.md)
     
    value = instance.GetComponent(componentHandle)  
  
C#|   
---|---  
      
    
    [CapturedSolidWorksComponent](topic14343.md) GetComponent( 
       ComponentHandle _componentHandle_
    )  
  
#### Parameters

 _componentHandle_
    A handle to the component for which to get capture data.

#### Return Value

The capture data associated with the given component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


