Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRootComponentHandles() Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) > [GetRootComponentHandles Method](topic13399.md) : GetRootComponentHandles() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an array of handles to all root components. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetRootComponentHandles() As ComponentHandle()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim value() As ComponentHandle
     
    value = instance.GetRootComponentHandles()  
  
C#|   
---|---  
      
    
    ComponentHandle[] GetRootComponentHandles()  
  
#### Return Value

An array of handles to all root components.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)   
[Overload List](topic13399.md)


