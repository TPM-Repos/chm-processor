![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSets Class](topic4143.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to give to the component set, if a null reference is specified, the file name of the base component (with an optional numeric suffix if required) will be used.

_capturedComponentId_
    The identifier of the captured component on which to base the component set.

Glossary Item Box

Adds a new project component set. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _capturedComponentId_ As Guid _
    ) As [ProjectComponentSet](topic4106.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSets](topic4143.md)
    Dim name As String
    Dim capturedComponentId As Guid
    Dim value As [ProjectComponentSet](topic4106.md)
     
    value = instance.Add(name, capturedComponentId)  
  
C#|   
---|---  
      
    
    public [ProjectComponentSet](topic4106.md) Add( 
       string _name_ ,
       Guid _capturedComponentId_
    )  
  
#### Parameters

 _name_
    The name to give to the component set, if a null reference is specified, the file name of the base component (with an optional numeric suffix if required) will be used.
_capturedComponentId_
    The identifier of the captured component on which to base the component set.

#### Return Value

The new project component set.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectComponentSets Class](topic4143.md)   
[ProjectComponentSets Members](topic4144.md)


