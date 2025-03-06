![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChangeComponentPath(Guid,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) > [ChangeComponentPath Method](topic3028.md) : ChangeComponentPath(Guid,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_originalComponentId_
    The unique identifier of the component to update.

_updatedComponentPath_
    The new path to the component.

Glossary Item Box

Updates the path of the specified component. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function ChangeComponentPath( _
       ByVal _originalComponentId_ As Guid, _
       ByVal _updatedComponentPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim originalComponentId As Guid
    Dim updatedComponentPath As String
    Dim value As Boolean
     
    value = instance.ChangeComponentPath(originalComponentId, updatedComponentPath)  
  
C#|   
---|---  
      
    
    public bool ChangeComponentPath( 
       Guid _originalComponentId_ ,
       string _updatedComponentPath_
    )  
  
#### Parameters

 _originalComponentId_
    The unique identifier of the component to update.
_updatedComponentPath_
    The new path to the component.

#### Return Value

True if the component was successfully rereferenced.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)   
[Overload List](topic3028.md)


