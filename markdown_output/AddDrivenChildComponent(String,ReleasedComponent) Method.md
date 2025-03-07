Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddDrivenChildComponent(String,ReleasedComponent) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentController Class](topic6252.md) > [AddDrivenChildComponent Method](topic6261.md) : AddDrivenChildComponent(String,ReleasedComponent) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_childMasterPath_
    The path to the child component to replace.

_childComponent_
    The component to add as a child.

Glossary Item Box

Adds a new component as a child of the component being released. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub AddDrivenChildComponent( _
       ByVal _childMasterPath_ As String, _
       ByVal _childComponent_ As [ReleasedComponent](topic6324.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentController](topic6252.md)
    Dim childMasterPath As String
    Dim childComponent As [ReleasedComponent](topic6324.md)
     
    instance.AddDrivenChildComponent(childMasterPath, childComponent)  
  
C#|   
---|---  
      
    
    public void AddDrivenChildComponent( 
       string _childMasterPath_ ,
       [ReleasedComponent](topic6324.md) _childComponent_
    )  
  
#### Parameters

 _childMasterPath_
    The path to the child component to replace.
_childComponent_
    The component to add as a child.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentController Class](topic6252.md)   
[ReleaseComponentController Members](topic6253.md)   
[Overload List](topic6261.md)


