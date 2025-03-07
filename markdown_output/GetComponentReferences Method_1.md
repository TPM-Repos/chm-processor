Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentReferences Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : GetComponentReferences Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_includeGeneratedParents_
    

_includeNotGeneratedParents_
    

_includeFailedParents_
    

_includeGeneratedChildren_
    

_includeNotGeneratedChildren_
    

_includeFailedChildren_
    

Glossary Item Box

Gets an object which will enumerate the released component references in the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetComponentReferences( _
       ByVal _includeGeneratedParents_ As Boolean, _
       ByVal _includeNotGeneratedParents_ As Boolean, _
       ByVal _includeFailedParents_ As Boolean, _
       ByVal _includeGeneratedChildren_ As Boolean, _
       ByVal _includeNotGeneratedChildren_ As Boolean, _
       ByVal _includeFailedChildren_ As Boolean _
    ) As [IGroupResultEnumerator(Of ReleasedComponentReferenceDetails)](topic2220.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim includeGeneratedParents As Boolean
    Dim includeNotGeneratedParents As Boolean
    Dim includeFailedParents As Boolean
    Dim includeGeneratedChildren As Boolean
    Dim includeNotGeneratedChildren As Boolean
    Dim includeFailedChildren As Boolean
    Dim value As [IGroupResultEnumerator(Of ReleasedComponentReferenceDetails)](topic2220.md)
     
    value = instance.GetComponentReferences(includeGeneratedParents, includeNotGeneratedParents, includeFailedParents, includeGeneratedChildren, includeNotGeneratedChildren, includeFailedChildren)  
  
C#|   
---|---  
      
    
    public [IGroupResultEnumerator<ReleasedComponentReferenceDetails>](topic2220.md) GetComponentReferences( 
       bool _includeGeneratedParents_ ,
       bool _includeNotGeneratedParents_ ,
       bool _includeFailedParents_ ,
       bool _includeGeneratedChildren_ ,
       bool _includeNotGeneratedChildren_ ,
       bool _includeFailedChildren_
    )  
  
#### Parameters

 _includeGeneratedParents_
    
_includeNotGeneratedParents_
    
_includeFailedParents_
    
_includeGeneratedChildren_
    
_includeNotGeneratedChildren_
    
_includeFailedChildren_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


