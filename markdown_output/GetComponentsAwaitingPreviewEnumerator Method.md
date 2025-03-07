Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentsAwaitingPreviewEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : GetComponentsAwaitingPreviewEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_topLevelOnly_
    True to only get top level (root) components.

Glossary Item Box

Gets an object which will enumerate the released components that are awaiting a preview in the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function GetComponentsAwaitingPreviewEnumerator( _
       ByVal _topLevelOnly_ As Boolean _
    ) As [IGroupResultEnumerator(Of ReleasedComponentDetails)](topic2220.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim topLevelOnly As Boolean
    Dim value As [IGroupResultEnumerator(Of ReleasedComponentDetails)](topic2220.md)
     
    value = instance.GetComponentsAwaitingPreviewEnumerator(topLevelOnly)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public [IGroupResultEnumerator<ReleasedComponentDetails>](topic2220.md) GetComponentsAwaitingPreviewEnumerator( 
       bool _topLevelOnly_
    )  
  
#### Parameters

 _topLevelOnly_
    True to only get top level (root) components.

#### Return Value

An enumerator for released components awaiting a preview in the group.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


