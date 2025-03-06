       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveComponentReference(ComponentHandle,ComponentHandle) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) > [RemoveComponentReference Method](topic13404.md) : RemoveComponentReference(ComponentHandle,ComponentHandle) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_parentHandle_
    The parent from which to remove the reference.

_childHandle_
    The child to remove from the parent.

Glossary Item Box

Uncaptures the specified child from the parent and returns the number of places where the child is still used. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function RemoveComponentReference( _
       ByVal _parentHandle_ As ComponentHandle, _
       ByVal _childHandle_ As ComponentHandle _
    ) As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim parentHandle As ComponentHandle
    Dim childHandle As ComponentHandle
    Dim value As Integer
     
    value = instance.RemoveComponentReference(parentHandle, childHandle)  
  
C#|   
---|---  
      
    
    int RemoveComponentReference( 
       ComponentHandle _parentHandle_ ,
       ComponentHandle _childHandle_
    )  
  
#### Parameters

 _parentHandle_
    The parent from which to remove the reference.
_childHandle_
    The child to remove from the parent.

#### Return Value

The number of parents which still hold a reference to the child after it is removed.

# Remarks

If the reference count drops to zero, then the child is completely removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)   
[Overload List](topic13404.md)


