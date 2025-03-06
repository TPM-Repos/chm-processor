       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryDeleteSpecification(Int32) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3400.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [TryDeleteSpecification Method](topic3398.md) : TryDeleteSpecification(Int32) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The unique numerical identifier of the specification to delete.

Glossary Item Box

Removes the given specification from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryDeleteSpecification( _
       ByVal _specificationId_ As Integer _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim value As Boolean
     
    value = instance.TryDeleteSpecification(specificationId)  
  
C#|   
---|---  
      
    
    public bool TryDeleteSpecification( 
       int _specificationId_
    )  
  
#### Parameters

 _specificationId_
    The unique numerical identifier of the specification to delete.

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
