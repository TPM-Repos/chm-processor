![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetState Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [States Class](topic11612.md) : GetState Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_stateId_
    The unique identifier of the state to get.

Glossary Item Box

Gets the state with the specified identifier. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetState( _
       ByVal _stateId_ As Guid _
    ) As [State](topic11559.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [States](topic11612.md)
    Dim stateId As Guid
    Dim value As [State](topic11559.md)
     
    value = instance.GetState(stateId)  
  
C#|   
---|---  
      
    
    public [State](topic11559.md) GetState( 
       Guid _stateId_
    )  
  
#### Parameters

 _stateId_
    The unique identifier of the state to get.

#### Return Value

The state with the specified identifier.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| Thrown if the specified state is not found.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[States Class](topic11612.md)   
[States Members](topic11613.md)


