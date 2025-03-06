       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetSpecification(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3404.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [TryGetSpecification Method](topic3402.md) : TryGetSpecification(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name associated with the specification to retrieve.

Glossary Item Box

Tries to get details about a specification with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetSpecification( _
       ByVal _name_ As String _
    ) As [SpecificationDetails](topic11292.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim name As String
    Dim value As [SpecificationDetails](topic11292.md)
     
    value = instance.TryGetSpecification(name)  
  
C#|   
---|---  
      
    
    public [SpecificationDetails](topic11292.md) TryGetSpecification( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name associated with the specification to retrieve.

#### Return Value

The specification details or a null reference if the specification doesn't exist.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3402.md)

©2024 DriveWorks Ltd. All Rights Reserved.
