Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRootComponentHandles(Boolean) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) > [GetRootComponentHandles Method](topic13399.md) : GetRootComponentHandles(Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_includeDeleted_
    Whether to include deleted components.

Glossary Item Box

Gets an array of handles to all root components. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetRootComponentHandles( _
       ByVal _includeDeleted_ As Boolean _
    ) As ComponentHandle()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim includeDeleted As Boolean
    Dim value() As ComponentHandle
     
    value = instance.GetRootComponentHandles(includeDeleted)  
  
C#|   
---|---  
      
    
    ComponentHandle[] GetRootComponentHandles( 
       bool _includeDeleted_
    )  
  
#### Parameters

 _includeDeleted_
    Whether to include deleted components.

#### Return Value

An array of handles to all root components.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)   
[Overload List](topic13399.md)


