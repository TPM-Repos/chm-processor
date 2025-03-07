Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyModifiedComponent Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : NotifyModifiedComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentHandle_
    A handle to the component that has changed.

Glossary Item Box

Notify the component manager that the given component has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyModifiedComponent( _
       ByVal _componentHandle_ As ComponentHandle _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim componentHandle As ComponentHandle
     
    instance.NotifyModifiedComponent(componentHandle)  
  
C#|   
---|---  
      
    
    void NotifyModifiedComponent( 
       ComponentHandle _componentHandle_
    )  
  
#### Parameters

 _componentHandle_
    A handle to the component that has changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


