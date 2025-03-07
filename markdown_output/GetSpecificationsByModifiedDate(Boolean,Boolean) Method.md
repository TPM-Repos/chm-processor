Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecificationsByModifiedDate(Boolean,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [GetSpecificationsByModifiedDate Method](topic3377.md) : GetSpecificationsByModifiedDate(Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_descending_
    True to retrieve specifications in reverse chronological order.

_includeArchived_
    True to also retrieve archived specifications.

Glossary Item Box

Gets specifications in chronological order. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetSpecificationsByModifiedDate( _
       ByVal _descending_ As Boolean, _
       ByVal _includeArchived_ As Boolean _
    ) As IEnumerable(Of SpecificationDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim descending As Boolean
    Dim includeArchived As Boolean
    Dim value As IEnumerable(Of SpecificationDetails)
     
    value = instance.GetSpecificationsByModifiedDate(descending, includeArchived)  
  
C#|   
---|---  
      
    
    public IEnumerable<SpecificationDetails> GetSpecificationsByModifiedDate( 
       bool _descending_ ,
       bool _includeArchived_
    )  
  
#### Parameters

 _descending_
    True to retrieve specifications in reverse chronological order.
_includeArchived_
    True to also retrieve archived specifications.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3377.md)


