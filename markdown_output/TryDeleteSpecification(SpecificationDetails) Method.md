       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryDeleteSpecification(SpecificationDetails) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3399.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [TryDeleteSpecification Method](topic3398.md) : TryDeleteSpecification(SpecificationDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationDetails_
    The details of the specification to delete.

Glossary Item Box

Removes the given specification from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryDeleteSpecification( _
       ByVal _specificationDetails_ As [SpecificationDetails](topic11292.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationDetails As [SpecificationDetails](topic11292.md)
    Dim value As Boolean
     
    value = instance.TryDeleteSpecification(specificationDetails)  
  
C#|   
---|---  
      
    
    public bool TryDeleteSpecification( 
       [SpecificationDetails](topic11292.md) _specificationDetails_
    )  
  
#### Parameters

 _specificationDetails_
    The details of the specification to delete.

#### Return Value

True if the specification existed and was removed, false if it doesn't exist.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3398.md)

©2024 DriveWorks Ltd. All Rights Reserved.
