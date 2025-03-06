![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsPermitted Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Teams Class](topic11737.md) : IsPermitted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamsToCheck_
    The unique identifier of the teams to check.

_currentUserId_
    The identifier of the user to check for permission.

_creatorId_
    The identifier of the specification's creator.

_ownerId_
    The identifier of the specification's owner.

Glossary Item Box

Checks to see if the team with the specified identifier is allowed according to the current access control list. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IsPermitted( _
       ByVal _teamsToCheck_() As Guid, _
       ByVal _currentUserId_ As Guid, _
       ByVal _creatorId_ As Guid, _
       ByVal _ownerId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Teams](topic11737.md)
    Dim teamsToCheck() As Guid
    Dim currentUserId As Guid
    Dim creatorId As Guid
    Dim ownerId As Guid
    Dim value As Boolean
     
    value = instance.IsPermitted(teamsToCheck, currentUserId, creatorId, ownerId)  
  
C#|   
---|---  
      
    
    public bool IsPermitted( 
       Guid[] _teamsToCheck_ ,
       Guid _currentUserId_ ,
       Guid _creatorId_ ,
       Guid _ownerId_
    )  
  
#### Parameters

 _teamsToCheck_
    The unique identifier of the teams to check.
_currentUserId_
    The identifier of the user to check for permission.
_creatorId_
    The identifier of the specification's creator.
_ownerId_
    The identifier of the specification's owner.

#### Return Value

True if the team with the specified identifier is allowed, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Teams Class](topic11737.md)   
[Teams Members](topic11738.md)


