       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveComponent Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : RemoveComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rootHandle_
    A handle to the component to remove.

Glossary Item Box

Removes the component with the given handle. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub RemoveComponent( _
       ByVal _rootHandle_ As ComponentHandle _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim rootHandle As ComponentHandle
     
    instance.RemoveComponent(rootHandle)  
  
C#|   
---|---  
      
    
    void RemoveComponent( 
       ComponentHandle _rootHandle_
    )  
  
#### Parameters

 _rootHandle_
    A handle to the component to remove.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


