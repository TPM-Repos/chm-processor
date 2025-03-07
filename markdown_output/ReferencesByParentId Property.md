Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReferencesByParentId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleasedComponentReferenceTree Interface](topic6106.md) : ReferencesByParentId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a map from a parent component's identifier to the references for that component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property ReferencesByParentId As IDictionary(Of Guid,IEnumerable(Of ReleasedComponentReferenceDetails))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleasedComponentReferenceTree](topic6106.md)
    Dim value As IDictionary(Of Guid,IEnumerable(Of ReleasedComponentReferenceDetails))
     
    value = instance.ReferencesByParentId  
  
C#|   
---|---  
      
    
    IDictionary<Guid,IEnumerable<ReleasedComponentReferenceDetails>> ReferencesByParentId {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleasedComponentReferenceTree Interface](topic6106.md)   
[IReleasedComponentReferenceTree Members](topic6107.md)


