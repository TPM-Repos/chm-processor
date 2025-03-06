![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddDrivenChildComponent(String,String,ReleasedComponent) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentController Class](topic6252.md) > [AddDrivenChildComponent Method](topic6261.md) : AddDrivenChildComponent(String,String,ReleasedComponent) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_childMasterPath_
    The path to the child component to replace.

_childMasterAddress_
    The optional address which further qualifies the child component to replace.

_childComponent_
    The component to add as a child.

Glossary Item Box

Adds a new component as a child of the component being released. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub AddDrivenChildComponent( _
       ByVal _childMasterPath_ As String, _
       ByVal _childMasterAddress_ As String, _
       ByVal _childComponent_ As [ReleasedComponent](topic6324.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentController](topic6252.md)
    Dim childMasterPath As String
    Dim childMasterAddress As String
    Dim childComponent As [ReleasedComponent](topic6324.md)
     
    instance.AddDrivenChildComponent(childMasterPath, childMasterAddress, childComponent)  
  
C#|   
---|---  
      
    
    public void AddDrivenChildComponent( 
       string _childMasterPath_ ,
       string _childMasterAddress_ ,
       [ReleasedComponent](topic6324.md) _childComponent_
    )  
  
#### Parameters

 _childMasterPath_
    The path to the child component to replace.
_childMasterAddress_
    The optional address which further qualifies the child component to replace.
_childComponent_
    The component to add as a child.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseComponentController Class](topic6252.md)   
[ReleaseComponentController Members](topic6253.md)   
[Overload List](topic6261.md)


