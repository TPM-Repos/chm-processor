Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteSpecification(SpecificationDetails) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [DeleteSpecification Method](topic3362.md) : DeleteSpecification(SpecificationDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationDetails_
    The specification to delete.

Glossary Item Box

Deletes the specification with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub DeleteSpecification( _
       ByVal _specificationDetails_ As [SpecificationDetails](topic11292.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationDetails As [SpecificationDetails](topic11292.md)
     
    instance.DeleteSpecification(specificationDetails)  
  
C#|   
---|---  
      
    
    public void DeleteSpecification( 
       [SpecificationDetails](topic11292.md) _specificationDetails_
    )  
  
#### Parameters

 _specificationDetails_
    The specification to delete.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| The specification does not exist.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3362.md)


