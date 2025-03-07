Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecificationComponents(Int32) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [GetSpecificationComponents Method](topic3372.md) : GetSpecificationComponents(Int32) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The numerical identifier of the specification for which to get reports.

Glossary Item Box

Gets released components on which the specification has a dependency. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetSpecificationComponents( _
       ByVal _specificationId_ As Integer _
    ) As IEnumerable(Of ReleasedComponentDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim value As IEnumerable(Of ReleasedComponentDetails)
     
    value = instance.GetSpecificationComponents(specificationId)  
  
C#|   
---|---  
      
    
    public IEnumerable<ReleasedComponentDetails> GetSpecificationComponents( 
       int _specificationId_
    )  
  
#### Parameters

 _specificationId_
    The numerical identifier of the specification for which to get reports.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3372.md)


